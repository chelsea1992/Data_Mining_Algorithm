import sys
import math

users = {}


def user_ave(user_a):
    num = 0
    user_sum = 0
    for k, v in user_a.iteritems():
        num += 1
        user_sum += v
    average = float(user_sum)/num
    return average


def pearson_correlation(user1, user2):
    product = 0
    sumUser1 = 0
    sumUser2 = 0
    user1_corated = []
    user2_corated = []
    numCount = 0
    sum1 = 0
    sum2 = 0

    for k, v in user1.iteritems():
        for i, j in user2.iteritems():
            if k == i:
                numCount += 1
                sumUser1 += v
                sumUser2 += j
                user1_corated.append(v)
                user2_corated.append(j)
    ave1 = sumUser1/numCount
    ave2 = sumUser2/numCount
    for i in range(0, len(user1_corated)):
        product += (user1_corated[i] - ave1)*(user2_corated[i] - ave2)
        sum1 += (user1_corated[i] - ave1)**2
        sum2 += (user2_corated[i] - ave2)**2
    sqrt_sum1 = float(math.sqrt(sum1))
    sqrt_sum2 = float(math.sqrt(sum2))
    if sqrt_sum1*sqrt_sum2 == 0:
        sim = -2
    else:
        sim = product/(sqrt_sum1*sqrt_sum2)
    return (sim, ave1)


def K_nearest_neighbors(user1, k):
    count_kuser = {}
    for key, value in users.iteritems():
        if key != user1:
                tuple_temp = pearson_correlation(users[key], users[user1])
                sim_with_user1 = tuple_temp[0]
                user1_average = tuple_temp[1]
                count_kuser[(key, user1_average)] = sim_with_user1
    count_kuser2 = count_kuser.items()
    sorted_count_kuser = sorted(count_kuser2, key=lambda item: (item[1], item[0][0]), reverse=True)
    sorted_count_list = []
    for itemj in sorted_count_kuser:
        if movie_predict in users[itemj[0][0]]:
            sorted_count_list.append([itemj[0][0],itemj[1],itemj[0][1]])
    if k > len(sorted_count_list):
        for i in range(0,len(sorted_count_list)):
            print sorted_count_list[i][0],sorted_count_list[i][1]
        return sorted_count_list[:len(sorted_count_list)]
    else:
        for i in range(0,k):
            print sorted_count_list[i][0],sorted_count_list[i][1]
        return sorted_count_list[:k]


def Predict(user1, item, k_nearest_neighbors):
    denominator = 0
    numerator = 0
    for i in k_nearest_neighbors:
        user_name = i[0]
        if item in users[user_name].keys():
            user_average = i[2]
            weight = i[1]
            numerator += (users[user_name][item] - user_average)*weight
            denominator += math.fabs(weight)
    predictNum = user_ave(users[user1]) + numerator/denominator
    return predictNum


if __name__ == '__main__':
    txt = open(sys.argv[1])
    for line in txt:
        lineList = line.strip().split("\t")
        if lineList[0] not in users:
            users[lineList[0]] = {}
            users[lineList[0]][lineList[2]] = float(lineList[1])
        else:
            users[lineList[0]][lineList[2]] = float(lineList[1])

    user_predict = sys.argv[2]
    movie_predict = sys.argv[3]
    k_value = int(sys.argv[4])
    k_nearest_neighbors_list = K_nearest_neighbors(user_predict, k_value)
    print Predict(user_predict, movie_predict, k_nearest_neighbors_list)


