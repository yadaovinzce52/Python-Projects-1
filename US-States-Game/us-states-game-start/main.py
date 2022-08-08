import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title='Guess the State', prompt='What\'s another state\'s name?')

data = pandas.read_csv('50_states.csv')
states = data['state'].to_list()
already_guessed = []
game_is_active = True

if answer_state in states and answer_state not in already_guessed:
    state = data[data['state'] == answer_state]
    x_coordinate = state['x']
    y_coordinate = state['y']



def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
