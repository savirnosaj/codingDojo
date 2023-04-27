# Assignment: Underscore
    # Create a custom Python module using OOP

class Underscore:
    def map(self, arr, callback):
        print("\n--- Map Method being Executed - Standby ...")
        for count in range(len(arr)):
            arr[count] = callback(arr[count])
        print(f"\n{arr}")
        return arr

    def find(self, arr, callback):
        print("\n--- Find Method being Executed - Standby ...")
        for count in range(len(arr)):
            if(callback(arr[count]) == True):
                print(f"\n{arr[count]}")
                return arr[count]

    def filter(self, arr, callback):
        print("\n--- Filter Method being Executed - Standby ...")
        results = []
        for count in range(len(arr)):
            if(callback(arr[count]) == True):
                results.append(arr[count])
        print(f"\n{results}")
        return results

    def reject(self, arr, callback):
        print("\n--- Reject Method being Executed - Standby ...")
        results = []
        for count in range(len(arr)):
            if(callback(arr[count]) == False):
                results.append(arr[count])
        print(f"\n{results}")
        return results

# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
timesBy2 = _.map([1,2,3], lambda x: x*2) # should return [2,4,6]                                                  # DONE
returnGreaterThan4 = _.find([1,2,3,4,5,6], lambda x: x>4) # should return the first value that is greater than 4  # DONE
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)   # should return [2,4,6]                               # DONE
odds = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0) # should return [1,3,5]                                  # DONE
