def hangmanAnimation_5(lives):
    if lives == 5:  #with all 5 lives
        a = print("""
   +------+
          |
          |
          |
          |
          |
          |
*************
        """)

    if lives == 4:  #with 4 lives
        a = print("""
   +------+
   |      |
          |
          |
          |
          |
          |
*************
        """)

    if lives == 3:  #with 3 lives
      a = print("""
   +------+
   |      |
   0      |
          |
          |
          |
          |
*************
        """)

    if lives == 2:  #with 2 lives
      a = print("""
   +------+
   |      |
   0      |
  \|/     |
          |
          |
          |
*************
        """)

    if lives == 1:  #with 1 life
        a = print("""
   +------+
   |      |
   0      |
  \|/     |
   |      |
          |
          |
*************
        """)

    

    if lives == 0:  #with 0 lives
        a = print("""
   +------+
   |      |
   0      |
  \|/     |
   |      |
  / \     |
          |
*************
\n""")
    return a
    



def hangmanAnimation_8(lives):
    if lives == 8:  #with all 5 lives
        a = print("""
   +------+
          |
          |
          |
          |
          |
          |
*************
        """)
        

    if lives == 7:  #with 4 lives
        a = print("""
   +------+
   |      |
          |
          |
          |
          |
          |
*************
        """)
        

    if lives == 6:  #with 3 lives
        a = print("""
   +------+
   |      |
   0      |
          |
          |
          |
          |
*************
        """)
        

    if lives == 5:  #with 2 lives
        a = print("""
   +------+
   |      |
   0      |
   |      |
          |
          |
          |
*************
        """)
        

    if lives == 4:  #with 2 lives
        a = print("""
   +------+
   |      |
   0      |
  \|      |
          |
          |
          |
*************
        """)
        

    if lives == 3:  #with 2 lives
        a = print("""
   +------+
   |      |
   0      |
  \|/     |
          |
          |
          |
*************
        """)
        

    if lives == 2:  #with 1 life
        a = print("""
   +------+
   |      |
   0      |
  \|/     |
   |      |
          |
          |
*************
        """)
        

    if lives == 1:  #with 1 life
        a = print("""
   +------+
   |      |
   0      |
  \|/     |
   |      |
  /       |
          |
*************
        """)
        

    if lives == 0:  #with 0 lives
        a = print("""
   +------+
   |      |
   0      |
  \|/     |
   |      |
  / \     |
          |
*************
\n""")
    
    return a