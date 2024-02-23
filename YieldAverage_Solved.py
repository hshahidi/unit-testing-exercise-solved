
class YieldAverage():
    """
    Assess Wafer Yield:
    This function checks the wafer lot for all the acceptance test criteria that were outlined.
    it will return the final list that passess all criteria.
    """
    def assess_wafer_yield(list):
        if len(list) == 0:
            raise ValueError("Error: Wafer lot is empty.")

        elif len(list) > 25:
            raise ValueError("Error: Wafer lot exceeds limit of 25 wafers.")

        else:
            for i, value in enumerate(list):
                if value is None:
                    del list[i]
                    
                else:
                    if isinstance(value, str):
                        list[i] = float(value)

                    elif  value > 100:
                        raise ValueError("Error: Values out of range. Please enter wafer yield as a decimal between 0 and 1.")
                        break

                    elif value < 0:
                        raise ValueError("Error: Values out of range. Please enter wafer yield as a decimal between 0 and 1.")
                        break

                    elif value > 1:
                        list[i] = round(float(value / 100), 4)               
        return list
    


    """
    Array Sum:
    Modularized Sum function that can be applied to any part of your code.
    """
    def array_sum(list):
        total = 0
        
        for i in list:
            total += i 
                        
        return total

    """
    Array Count:
    Modularized Count function that can be applied to any part of your code.
    """
    def array_count(list):
        count = 0
        for i in list:
            count += 1
        return count


    """
    Divide:
    Returns the divided result with additional error handling for division by zero.
    Promotes modularization with the code.
    """
    def divide(numerator, denominator):
        if denominator == 0:
            raise ValueError("Error: Cannot divide by zero.")
        else:
            return round(numerator/denominator, 4)


    """
    Lot Yield Average:
    This function first passes the wafer lot to assess_wafer_yield to check if all criteria pass.
    Then the checked list is passed into the other functions for computing average.
    """
    def lot_yield_average(list):
        checked_list = assess_wafer_yield(list)
        return divide(array_sum(checked_list), array_count(checked_list))

        


    



