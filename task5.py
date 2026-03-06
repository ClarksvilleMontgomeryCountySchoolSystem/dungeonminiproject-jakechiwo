Bad = r"""
       .----------.
      /  .-.  .-.  \
     /   | |  | |   \
     \   `-'  `-'  _/
     /\     .--.  / |
     \ |   /  /  / /
     / |  `--'  /\ \
      /`-------'  \ \ 
"""
Good = r"""
   _.-.-=-.                  .-=.'"=.-=.
  (       .'    \  :  /     '._.-=._.=-'
   '-"-=="    `. .-=-. .'  
----------------'     '------------[TomekK]-------"""
escaped = True
if escaped:
    print(Good)
    outcome = "Legend: You are finally able to leave, your name etching into the wall with a phenomena you can't quite explain, as you sprint for freedom."
else:
    print(Bad)
    outcome = "Doom: You are left helplessly in the dungeon, your screams to reach only the next unfortunate traveller that enters this tomb."
print(outcome)
