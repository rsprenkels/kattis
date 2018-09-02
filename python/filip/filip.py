class filip:

    def giveLargest(self):
        first, second = input().split(' ')
        first, second = first[::-1], second[::-1]
        if(int(first) > int(second)):
            return first
        else:
            return second

if __name__ == '__main__':
    print(filip().giveLargest())
