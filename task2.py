Good = r"""      
   ,-' ;  ! `-.
  / :  !  :  . \
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|"""
Bad = r"""                 _
                   _____(O)_____
                  /             \
                 /               \    ___
              __/       1 7       \  (   )      __
      __   __( /                   \__) (_     (  )
     (  \ (   /     T O N N E S     \    _)_    )/
      )  \_) /                       \   )( )  (_)
   _ (__    /                         \ (_/(__   ___
  (_) __)  /___________________________\      ) (   )
     (___                                  _ /   )  )
        (       ___                   ____/ ))  (__/
    _(\  ) _   (   )  __      ____  __)  _ ( \_
   (___)(_/ )   \ (  (  \    (    )(   _/ ) \__)
           (_____) \  ) (   __)  / /  (  (_
            _       )(   \ (    (_/    )   )
           (_)     (__)  (  )  _      (___/
                          )/  (_)
                          '"""
has_key = True
if has_key:
    outcome = "Click: The door opens slowly, creaking before coming to a sudden halt."
    print(Good)
else:
    outcome = "Doom: A latch above the door snapped, a large weight fell onto your head, crushing you."
    print(Bad)
print(outcome)
