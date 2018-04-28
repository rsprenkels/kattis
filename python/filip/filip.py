class filip:

    def giveLargest(self):
        first, second = input().split(' ')
        if(first > second):
            return first
        else:
            return second

if __name__ == '__main__':
    print(filip().giveLargest())
