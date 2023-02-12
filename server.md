User
----Users
    -email
    -first name , last name
    -birth date
    -gender
    -country
    -language
    -currency
    -is_artist

Medias
----Photo
    -owner
    -imagefile
    -imageurl
    -worklog
    -kind #worklog, music albums

----Video
    -owner
    -videofile
    -videourl
    -worklog

----Music
    -title
    -artist
    -image
    -audio_file
    -audio-url
    -duration
    -description
    -ganre

    
Feed    
----Feeds : 모든 유저마다 하나의 피드가 존재한다.
    -users
    -payloads
    -backgroundimgs
    -worklogs
    -chattingrooms
    -votes
----WorkLog : feed 와 1:다
    -poster
    -posted_feed
    -payload
    -photo
    -is_shop
    -video
----Vote : feed 와 다대다
    -owner
    -payload
    -voteentry

ChattingRoom
----ChattingRooms(DirectMassesges)
    -sendbird or dm

Wallet
----Wallets : 모든 유저마다 하나의 지갑이 존재한다.
    -owner
    -payment method
    -bisou
    -account
    -bank

PlayList
----PlayLists
    -owner
    -description
    -musics
    -hashtag
Produces

Shops

Common
----CommonModel
    -created_at
    -upadated_at

Review
----Reviews
    -writer
    -worklog
    -payload

Refferal
----Refferals
    -user
    -introducer

Point
----Points
    -user
    -nowbisou
    -usedpoint
    -chargedpoint
    -pointswithdrawn

Produce
----Donations
    -fromuser
    -touser
    -method(choosen) #어느방법으로 donations을 했는가
    -amount

Ticketing
----Ticketings
    -performance
    -user
    -start_at
    -end_at
    


Bank of America Alabama

051000017

Bank of America Alaska

051000018

Bank of America Arizona

122101706

Bank of America Arkansas

082000073

Bank of America California

121000358

Bank of America Colorado

123103716

Bank of America Connecticut

011900254

Bank of America Delaware

031202084

Bank of America District of Columbia

054001204

Bank of America Florida

063100277/ 063000047

Bank of America Florida, West

063100277

Bank of America Georgia

061000052

Bank of America Hawaii

051000017

Bank of America Idaho

123103716

Bank of America Illinois

081904808

Bank of America Illinois, North

071000505

Bank of America Illinois, Chicago Metro

081904808/ 0071103619

Bank of America Indiana

071214579

Bank of America Iowa

073000176

Bank of America Kansas

101100045

Bank of America Kentucky

051000017

Bank of America Louisiana

051000017

Bank of America Maine

011200365

Bank of America Maryland

052001633

Bank of America Massachusetts

011000138

Bank of America Michigan

072000805

Bank of America Minnesota

071214579

Bank of America Mississippi

051000017

Bank of America Missouri, East

081000032/ 101000035

Bank of America Missouri, West

081000033

Bank of America Montana

051000017

Bank of America Nebraska

051000017

Bank of America Nevada

122400724

Bank of America New Hampshire

011400495

Bank of America New Jersey

021200339

Bank of America New Mexico

107000327

Bank of America New York

021000322

Bank of America North Carolina

053000196

Bank of America North Dakota

051000017

Bank of America Ohio

051000017

Bank of America Oklahoma

103000017

Bank of America Oregon

323070380

Bank of America Pennsylvania

031202084

Bank of America Rhode Island

011500010

Bank of America South Carolina

053904483

Bank of America South Dakota

051000017

Bank of America Tennessee

064000020

Bank of America Texas, North

111000025

Bank of America Texas

111000025/ 113000023

Bank of America Utah

051000017

Bank of America Vermont

051000017

Bank of America Virginia

051000017

Bank of America Washington

125000024

Bank of America West Virginia

051000017

Bank of America Wisconsin

051000017

Bank of America Wyoming

051000017

