# -*- coding: cp1252 -*-

#http://www.lbp.police.uk/information/latest_news/news_archives/2013/february-1.aspx
#http://www.lbp.police.uk/information/latest_news/news_archives/2013.aspx
#http://www.lbp.police.uk/information/latest_news/news_archives.aspx

s1 = '''Lothian and Borders Police are appealing for witnesses following a report of indecent exposure in Edinburgh.

The incident happened around 7.50pm on Tuesday 5 February, in the Leith area of the city.

A 33-year-old woman was walking home and reached the crossroads of Iona Street and Dickson Street when a man approached her before exposing himself.

The suspect then made off towards Easter Road where he was lost to sight. The victim returned home and contacted police.

Officers are now urging anyone who can assist with their enquiries to contact police immediately.

The suspect is described as white, around 5ft 6ins tall with an average build, fresh-faced and clean-shaven complexion. He was wearing a dark hooded top with yellow writing on the chest, grey jogging bottoms, a black shoulder bag and spoke with a Scottish accent.

A police spokesperson said: "The suspect exposed himself to the woman and made an inappropriate remark before running off.

"While she was uninjured, the victim was understandably distressed and we are keen to hear from anyone who remembers seeing anything suspicious in or around Iona Street on Tuesday evening.

"Similarly, anyone who recognises the description of the suspect is also asked to come forward."

Those with information can contact Lothian and Borders Police on 0131 311 3131, or the charity Crimestoppers in complete anonymity on 0800 555 111.'''

s2 = '''Lothian and Borders Police are appealing for witnesses after an elderly woman was assaulted and robbed in Edinburgh.

The 81-year-old was walking in Wester Hailes Road towards the Wester Hailes Plaza at around 7pm yesterday and began climbing the stairs of the footbridge.

At this time a male youth approached her and grabbed at her handbag and a carrier bag she was holding.

As a result of the struggle the victim fell down a number of stairs and injured her arm and shoulder.

The suspect then made off with the woman's bags and was pursued by a member of the public before being lost to sight.

A man, who was with his young daughter, then helped the victim to her feet and she returned home before contacting police and attending at hospital where she continues to be treated.

Police are now urging anyone who can assist with their enquiries to come forward.

The first suspect is described as white, 16 or 17-years-old and wearing a light coloured two-tone hooded top, light coloured jogging bottoms and trainers.

A police spokesman said: "As well as being extremely upset by the theft of her bags, the elderly woman also suffered a painful injury to her arm and shoulder, which required treatment.

"Anyone who was in the Wester Hailes Road area yesterday evening and remembers seeing anything suspicious is asked to contact police immediately.

"We are particularly keen to trace the member of the public who helped the victim up after her fall and would ask him to get in touch as soon as possible."

Those with information can contact Lothian and Borders Police on 0131 311 3131, or the charity Crimestoppers in complete anonymity on 0800 555 111.'''

s3 = '''Police in East Lothian are appealing for witnesses following a bogus caller incident in Port Seton on Tuesday, 5 February.

The suspect walked into the address in Inglis Avenue without invitation and claimed that he was there to fix the homeowner's satellite television system.

He then examined the satellite box, appearing to fumble with the cables, before demanding the owner pay £30 for his services.

The suspect produced what appeared to be a chip and pin device, and asked the owner to enter his bank card and supply his pin number. The owner refused, and the suspect left the house empty-handed.

He is described as white, in his 20s, 5ft 8ins tall, slim build, dark clothing, with a Fife accent.

A Lothian and Borders Police spokesman said: "We are appealing to anyone in the Port Seton area who received any kind of unsolicited visit by a man claiming to be there to check their satellite system, or carry out any kind of electrical or maintenance work, to contact police.

"Similarly, anyone who noticed a man matching the description of the suspect in Inglis Avenue or elsewhere in the local area should also get in touch.

"At this time we are warning residents to be mindful of the dangers posed by bogus callers.

"Anyone who receives an unsolicited call at their home by anyone offering to carry out maintenance or any other kind of work should deny them entry.

"If they claim to be from a utilities company then residents should check their identification, and if still in doubt, contact the company they claim to represent.

"If residents are suspicious as to the intentions of any cold caller then they should contact the police."

Anyone with any information should contact Lothian and Borders Police on 0131 311 3131, or Crimestoppers, where information can be reported anonymously, on 0800 555 111.'''

road_names = ['avenue','street','road','estate','lane']

get_street_locations = lambda split_report: filter(lambda (x,y): y.lower() in road_names and y.istitle(),enumerate(split_report))

explode_report = lambda report: filter(lambda x: len(x)>0, x.report.replace('\n',' ').split(' '))
