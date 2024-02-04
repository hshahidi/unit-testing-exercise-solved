def wafer_yield_sum(list):
    total = 0

    for i in list:
        if i is None or isinstance(i, str):
            continue
        elif i > 100:
            raise ValueError("Error: Values out of range. Please enter wafer yield as a decimal between 0 and 1.")
            break
        elif i < 0:
            raise ValueError("Error: Values out of range. Please enter wafer yield as a decimal between 0 and 1.")
            break
        else:
            #converting percents into their decimal equivalents
            if i > 1:
                i = i / 100
                total += i
            else:
                total += i 
                    
    return round(total, 4)

  
def wafer_yield_count(list):
    count = 0
    if len(list) == 0:
        raise ValueError("Error: Wafer lot is empty.")
        
    for i in list:
        if i is None or isinstance(i, str):
            continue
        elif len(list) > 25:
            raise ValueError("Error: Wafer lot exceeds limit of 25 wafers.")
            break
        else:
            count += 1
            
    return count


def divide(numerator, denominator):
    return round(numerator/denominator, 4)


def lot_yield_average(list):
    return divide(wafer_yield_sum(list), wafer_yield_count(list))



