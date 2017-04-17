import sys
import math


def distance(list1,list2):
    dis = 0
    for i in range(0,point_dimension):
        dis += (list1[i]-list2[i])**2
    sqrt_dis = math.sqrt(dis)
    return sqrt_dis


def re_center(listc):
    center_sum = [0 for i in range(point_dimension)]
    center = []
    num = len(listc)
    for i in range(0, point_dimension):
        for item in listc:
            center_sum[i] += item[i]
    for j in center_sum:
        center.append(j/num)
    return center


def convert(listin):
    lista = listin[:]
    conv = []
    for i in range(6):
        conv.append(dict())
    conv[0]['low'] = 1.0/4.0
    conv[0]['med'] = 2.0/4.0
    conv[0]['high'] = 3.0/4.0
    conv[0]['vhigh'] = 4.0/4.0
    conv[1] = conv[0]
    conv[2]['5more'] = 4.0/4.0
    for j in range(2, 5):
        conv[2][str(j)] = (j-1.0)/4.0
    conv[3]['more'] = 3.0/3.0
    conv[3]['2'] = 1.0/3.0
    conv[3]['4'] = 2.0/3.0
    conv[4]['small'] = 1.0/3.0
    conv[4]['med'] = 2.0/3.0
    conv[4]['big'] = 3.0/3.0
    conv[5]['low'] = 1.0/3.0
    conv[5]['med'] = 2.0/3.0
    conv[5]['high'] = 3.0/3.0
    for i in range(len(lista)-1):
        lista[i] = conv[i][lista[i]]
    return lista

def cluster_name(listd):
    count_name_frequency = {}
    for point_d in listd:
        count_name_frequency[point_d[point_dimension]] = count_name_frequency.setdefault(point_d[point_dimension], 0) + 1
    items_frequency = count_name_frequency.items()
    sorted_frequency = sorted(items_frequency,key=lambda item:item[1],reverse=True)
    return sorted_frequency[0][0]


if __name__ == '__main__':
    dataList = []
    raw_data_list = []
    raw_data_txt = open(sys.argv[1])
    center_txt = open(sys.argv[2])
    cluster_num = int(sys.argv[3])
    iter = int(sys.argv[4])
    center_list = []

    for line in raw_data_txt:
        lineList = line.strip().split(",")
        point_dimension = len(lineList) - 1
        raw_data_list.append(lineList)
        dataList.append(convert(lineList))
    #print dataList
    for line2 in center_txt:
        lineList2 = line2.strip().split(",")
        center_list.append(convert(lineList2))

    for iter_num in range(iter):
        clusters = [[] for i in range(cluster_num)]
        for point in dataList:
            dis_min = 90000000
            for center_point in center_list:
                dis_temp = distance(point,center_point)
                if dis_temp < dis_min:
                    dis_min = dis_temp
                    min_center = center_point
            clusters[center_list.index(min_center)].append(point)
        center_list = []
        wrong_assigned = 0
        with open("qiaozhi_song_output", "w") as outfile:
            for cluster in clusters:
                center_list.append(re_center(cluster))
                if iter_num == iter - 1:
                    # print "cluster:",cluster_name(cluster)
                    outfile.write("\n"+"\n"+"cluster:" + " " + cluster_name(cluster) +"\n")
                    for point in cluster:
                        # print raw_data_list[dataList.index(point)]
                        temp = raw_data_list[dataList.index(point)]
                        # outfile.write("["+", ".join(temp)+"]" + "\n")
                        outfile.write(str(temp)+ "\n")
                        if point[point_dimension] != cluster_name(cluster):
                            wrong_assigned += 1
            outfile.write("\n"+"\n"+"Number of points wrongly assigned:"+"\n")
            outfile.write(str(wrong_assigned))

with open("qiaozhi_song_output", 'r') as fin:
    data = fin.read().splitlines(True)
with open("qiaozhi_song_output", 'w') as fout:
    fout.writelines(data[2:])



