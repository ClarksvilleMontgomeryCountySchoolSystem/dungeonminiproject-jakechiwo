Good = r"""          __,---.__
       ,-'         `-.
     ,'               `.
    /                   \
   /         .           \
  ;           )           :
  |          ((           |
  |          ) \          |
  :         ( , )         ;
   \       _ `|'__       /
    \        ( _ )      /
     `.    )/(/( \|   ,'
       `- ()  )()|| -'
           | ()  ||
           |     ||
           |     ()
           |     |
           |     |
           |     |
           |     |
       ____|_____|____
      (________    ___)
         \___     _/
         (_____  __)
          \       /
           )__   (
          (____  _)
            |   |
            |   |
            |   |
            |   |
            |   |
            |   |
            |   |
          _/     \_
     .--'_________`--."""
Bad = r"""               ,////,
                        /// 6|
                        //  _|
                       _/_,-'
                  _.-/'/   \   ,/;,
               ,-' /'  \_   \ / _/
               `\ /     _/\  ` /
                 |     /,  `\_/
                 |     \'
 pb  /\_        /`      /\
   /' /_``--.__/\  `,. /  \
  |_/`  `-._     `\/  `\   `.
            `-.__/'     `\   |
                          `\  \
                            `\ \
                              \_\__
                               \___)"""
torch_lit = True
if torch_lit:
    outcome = "Flicker: You found a candle against the dungeon flooring, as you picked it up it lit up impossibly, use it to light your travels"
    print(Good)
else:
    outcome = "Doom: You ran around helplessly in the suffocating Dungeon, unable to find an opening on the sleek walls of stone, dying from exhaustion."
    print(Bad)
print(outcome)