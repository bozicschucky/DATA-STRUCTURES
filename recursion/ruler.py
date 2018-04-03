def draw_line(tick_lenght, tick_label=''):
    """
    Draw one line with given tick lenght( followed by optional label.)
    """
    line = '-'*tick_lenght
    if tick_label:
        line += ' '+tick_label
        print(line)

def draw_interval(center_length):
    '''
    Draw tick interval based upon a central tick lenght
    '''
    if center_length > 0:    #stop when lenght is 0
        draw_interval(center_length-1 )
        print(center_length)
        print(draw_interval(center_length-1))




def draw_ruler(num_inches,major_lenght):
    """
    Draw English ruler with given num of inches, major tick lenght
    """
    draw_line(major_lenght,'0') #draw inch 0 line
    for j in range(1,1+num_inches):
        print(draw_interval(major_lenght-1))   #draw interior ticks for inch
        draw_line(major_lenght,str(j))  #draw inch j line and label

#draw_ruler(10,3)

draw_interval(10)
