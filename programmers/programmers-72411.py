from itertools import combinations


def solution(orders, course):
    answer = []
    
    for num in course:
        menus = {}
        count = 0
        
        for order in orders:
            order = set(order)
            
            for menu in list(combinations(order, num)):
                menu = ''.join(sorted(menu))
                
                if menu not in menus:
                    menus[menu] = 1
                else:
                    menus[menu] += 1
                
                count = count if count > menus[menu] else menus[menu]
        
        if count >= 2:
            for menu in menus:
                if menus[menu] == count:
                    answer.append(menu)
    
    return sorted(answer)