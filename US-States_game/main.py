import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
states = data['state'].to_list()
already_guessed = []

while len(already_guessed) < 50:
    answer_state = screen.textinput(title=f'{len(already_guessed)}/50 States Guessed',
                                    prompt='What\'s another state\'s name?').title()

    if answer_state == 'Exit':
        break
    if answer_state in states and answer_state not in already_guessed:
        already_guessed.append(answer_state)
        states.remove(answer_state)
        state = data[data['state'] == answer_state]
        x_coordinate = int(state['x'])
        y_coordinate = int(state['y'])
        state_write = turtle.Turtle()
        state_write.hideturtle()
        state_write.penup()
        state_write.color('black')
        state_write.goto(x_coordinate, y_coordinate)
        state_write.write(answer_state)

df = pandas.DataFrame(states)
df.to_csv('states_to_learn.csv')
