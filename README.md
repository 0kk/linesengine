# LinesEngine
App for email domain handling.

	 

  __                  ______                        _,   __   __ 
 ( /   o             (  /              o           ( |  / /  /  )
  /   ,  _ _   _  (    /--   _ _   _, ,  _ _   _     | / /  /  / 
(/___/(_/ / /_(/_/_)_(/____// / /_(_)_(_/ / /_(/_    |/ / o(__/  
                                   /|                            
                                  (/                             
                                                                                                                    
						[by 0kk]
-----------------------------------------------
	 
	 
	./linesengine.py [options]
	 
	options:
	 
	-i,--url     [::] Input db file 
	-o,--output  [::] Output result file
	-p,--packing [::] Packing of lines
	 
	[+] usage:
	 
	./linesengine.py -i db.txt -o db_result.txt
	./linesengine.py -i db.txt -o db_result.txt -p true
  
  
  ----------Raw input example
j.doe@gmail.com:1111111
lnk@qip.ru:22222222
qwerty@web.de;12121212
qwerty@italy.it;222222222q
qw23e@web.de:21212121
gg@web.de:qwqwqw

  ----------Output example (-p false)
  
   (env) $python linesengine.py -i input.txt -o stats.txt
Processing db of lines...: 6it [00:00, 12690.78it/s]
Sorting tuples...: 100%|#######################| 4/4 [00:00<00:00, 39290.90it/s]
Creating of table...: 100%|####################| 4/4 [00:00<00:00, 20044.46it/s]
[+] Done
[+] Saved at stats.txt

-----------Stats.txt
[DOMAINS] 

+-----------+-------+
|  Domains  | Count |
+-----------+-------+
|  web.de   |   3   |
+-----------+-------+
|  qip.ru   |   1   |
+-----------+-------+
| italy.it  |   1   |
+-----------+-------+
| gmail.com |   1   |
+-----------+-------+

------------With '-p true' arg

.../packed$ tree.
├── gmail.com
│   └── gmail.com.txt
├── italy.it
│   └── italy.it.txt
├── qip.ru
│   └── qip.ru.txt
└── web.de
    └── web.de.txt

4 directories, 4 files

-------------

.../packed/web.de$ cat web.de.txt
qwerty@web.de:12121212

qw23e@web.de:21212121

gg@web.de:qwqwqw




 
