import random

template = [
"""
         _                      _______                      _
      _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_
     dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb
     V      ~"Mb          dOOOOOOOOOOOOOOOOOb          dM"~      V
              `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'
               `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'
          __     `YMMM| OP'~"YOOOOOOOOOOOP"~`YO |MMMP'     __
        ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.
     _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._
                 `YMMMM\`OOOo     OOO     oOOO'/MMMMP'
         ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.
       ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.
      ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.
      MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM
      YMb           ~YMMMM\`OOOOI`````IOOOOO'/MMMMP~           dMP
       `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'
         `'                  `OObNNNNNdOO'                   `'
                               `~OOOOO~'
""",
"""
                 ,----------------,              ,---------,
            ,-----------------------,          ,"        ,"|
          ,"                      ,"|        ,"        ,"  |
         +-----------------------+  |      ,"        ,"    |
         |  .-----------------.  |  |     +---------+      |
         |  |                 |  |  |     | -==----'|      |
         |  |                 |  |  |     |         |      |
         |  |                 |  |  |/----|`---=    |      |
         |  |                 |  |  |   ,/|==== ooo |      ;
         |  |                 |  |  |  // |(((( [33]|    ,"
         |  `-----------------'  |," .;'| |((((     |  ,"
         +-----------------------+  ;;  | |         |," 
            /_)______________(_/  //'   | +---------+
       ___________________________/___  `,
      /  oooooooooooooooo  .o.  oooo /,   \,"-----------
     / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
    /_==__==========__==_ooo__ooo=_/'   /___________,"
""",
"""
                     .                          
                     M                          
                    dM                          
                    MMr                         
                   4MMML                  .     
                   MMMMM.                xf     
   .              "MMMMM               .MM-     
    Mh..          +MMMMMM            .MMMM      
    .MMM.         .MMMMML.          MMMMMh      
     )MMMh.        MMMMMM         MMMMMMM       
      3MMMMx.     'MMMMMMf      xnMMMMMM"       
      '*MMMMM      MMMMMM.     nMMMMMMP"        
        *MMMMMx    "MMMMM\    .MMMMMMM=         
         *MMMMMh   "MMMMM"   JMMMMMMP           
           MMMMMM   3MMMM.  dMMMMMM            .
            MMMMMM  "MMMM  .MMMMM(        .nnMP"
=..          *MMMMx  MMM"  dMMMM"    .nnMMMMM*  
  "MMn...     'MMMMr 'MM   MMM"   .nMMMMMMM*"   
   "4MMMMnn..   *MMM  MM  MMP"  .dMMMMMMM""     
     ^MMMMMMMMx.  *ML "M .M*  .MMMMMM**"        
        *PMMMMMMhn. *x > M  .MMMM**""           
           ""**MMMMhx/.h/ .=*"                  
                    .3P"%....                   
                  nP"     "*MMnx 
"""]

logo = random.choice(template)
