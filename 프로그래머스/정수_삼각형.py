# 예전꺼
# def solution(triangle):
#     answer = triangle[0][0]
#     cur_list = triangle[0]

#     if len(triangle) == 1:
#         return answer

#     for next_list in triangle[1:]:
#         sum_list = []
#         for i in range(len(cur_list)):
#             if i == 0:
#                 sum_list.append(cur_list[i] + next_list[i])
#                 sum_list.append(cur_list[i] + next_list[i+1])
#             else:
#                 sum_list[i] = max(sum_list[i], cur_list[i] + next_list[i])
#                 sum_list.append(cur_list[i] + next_list[i+1])
#         cur_list = sum_list

#     return max(sum_list)

# 이번꺼
def solution(triangle):
    for i in range(len(triangle)-1,0,-1):
        for j in range(len(triangle[i-1])):
            triangle[i-1][j] += max(triangle[i][j],triangle[i][j+1])
    return triangle[0][0]