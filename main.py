"""
   ----- PROBLEM -----
   - A set of Rectangular Cardboards are arranged on the X Y axis, the inputs are cardboard indices in the format (x1,x2,h),

     x1 - Begin Index X Axis
     x2 - End Index X Axis
     h - Height (Y  Axis)

Cardboards can be  arranged in the intersecting manner, partially or fully subsumed, as a solution listing the outline listing the rise and drop. For the example given below, following is the:

Input  - [(1,5,10),(4,6,8),(10,15,10),(11,12,8)]
Output - [(1,10),(5,8),(6,0),(10,10),(15,0)]
"""


def get_outer_boundary(input):
    input.sort(key=lambda k: (k[0], -k[2]))
    output = []
    right_most_x = 0
    for i in range(len(input)):
        if i == 0:
            output.append((input[i][0], input[i][2]))
        else:
            if input[i][1] >= input[i - 1][1] >= input[i][0]:
                if input[i][2] < input[i - 1][2]:
                    output.append((input[i - 1][1], input[i][2]))
                if input[i][2] > input[i - 1][2]:
                    output.append((input[i][0], input[i][2]))

            if input[i][1] < input[i - 1][1] and input[i][0] <= input[i - 1][1]:
                if input[i][2] > input[i - 1][2]:
                    output.append((input[i][0], input[i][2]))
                    output.append((input[i][1], input[i - 1][2]))

            if input[i][1] >= input[i - 1][1] and input[i][0] > input[i - 1][1]:
                output.append((input[i - 1][1], 0))
                output.append((input[i][0], input[i][2]))

        if input[i][1] > right_most_x:
            right_most_x = input[i][1]

    output.append((right_most_x, 0))
    return output


if __name__ == '__main__':
    input1 = [(1, 5, 10), (4, 6, 8), (10, 15, 10), (11, 12, 8)]
    input2 = [(1, 10, 4), (1, 8, 6), (1, 6, 8)]
    input3 = [(0, 6, 2), (5, 10, 8), (7, 8, 12)]
    output = get_outer_boundary(input1)
    print(output)
    output = get_outer_boundary(input2)
    print(output)
    output = get_outer_boundary(input3)
    print(output)
