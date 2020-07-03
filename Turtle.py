import turtle as t # korzystamy z pliku turtle.py

window = t.Screen() # tworzy nam okno programu
turtle = t.Turtle() # tworzymy element na którym będziemy rysować

turtle.hideturtle() # usuwa strzałkę na początku

turtle.forward(150) # rysuje nam 150 pikseli prosto
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(150)

turtle.hideturtle() # usuwa strzałkę na końcu


window.mainloop() # okno nam się nie zamyka

