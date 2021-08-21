--- random sampling 2000 filings
SELECT * FROM edgar_company_filing order by rand() limit 2000;

--- select the files of gaven filing id
SELECT * FROM edgar_filing_file WHERE 
doc_name is not null and doc_type <> 'GRAPHIC' and
filing_id in (
	'6802',
'48813',
'75920',
'227782',
'13747',
'53354',
'48733',
'359777',
'84953',
'330353',
'254390',
'207152',
'248083',
'258194',
'284633',
'214615',
'8243',
'245506',
'311857',
'36414',
'332339',
'68129',
'6726',
'119046',
'234118',
'43575',
'53217',
'207784',
'3796',
'188139',
'287670',
'130369',
'248844',
'210508',
'130999',
'223153',
'108407',
'124482',
'281802',
'146009',
'281227',
'327788',
'265938',
'343718',
'177699',
'44510',
'17930',
'343673',
'150459',
'137138',
'81932',
'260092',
'291502',
'294185',
'245184',
'316715',
'194315',
'161126',
'45066',
'88148',
'276388',
'128686',
'293937',
'210829',
'305872',
'104012',
'25663',
'280873',
'88016',
'63602',
'70824',
'76797',
'89922',
'311529',
'98870',
'79454',
'258720',
'231363',
'366290',
'219985',
'43278',
'214066',
'299565',
'295980',
'125094',
'358676',
'191610',
'77414',
'132393',
'115162',
'315025',
'84965',
'251511',
'105014',
'271081',
'11925',
'116298',
'194007',
'84413',
'169969',
'271233',
'317433',
'207454',
'69078',
'181217',
'224850',
'77687',
'315955',
'6154',
'27880',
'230299',
'162918',
'150431',
'332181',
'277712',
'247481',
'172661',
'366070',
'257121',
'3346',
'357362',
'220142',
'220031',
'174611',
'285680',
'335184',
'267275',
'11682',
'19894',
'331795',
'67035',
'245103',
'292585',
'290219',
'223516',
'248452',
'361941',
'252396',
'211852',
'313599',
'156886',
'264787',
'190629',
'253029',
'194824',
'257886',
'290725',
'202150',
'224328',
'186069',
'89291',
'140393',
'241956',
'277895',
'355271',
'101755',
'273170',
'108305',
'340829',
'138349',
'161608',
'327119',
'348715',
'239583',
'2722',
'25015',
'287465',
'25783',
'225712',
'54015',
'259608',
'238032',
'202107',
'279889',
'135201',
'251213',
'208576',
'85512',
'48796',
'192362',
'224665',
'2455',
'137201',
'116512',
'176519',
'294699',
'312912',
'63449',
'153974',
'126610',
'284240',
'77342',
'130757',
'152385',
'200706',
'250949',
'129370',
'349221',
'120434',
'141839',
'328306',
'299750',
'156165',
'64037',
'266837',
'49738',
'140802',
'350289',
'201926',
'328001',
'330953',
'61860',
'183912',
'148095',
'35402',
'273669',
'140990',
'240853',
'336931',
'318460',
'288044',
'59075',
'76420',
'273986',
'2236',
'312044',
'235207',
'146287',
'191263',
'12422',
'290260',
'344516',
'102711',
'250402',
'357004',
'335079',
'143371',
'339919',
'325009',
'268288',
'190652',
'119278',
'76660',
'148156',
'171287',
'186852',
'129661',
'192996',
'183754',
'142880',
'191338',
'338780',
'151853',
'172842',
'114131',
'238089',
'328175',
'174854',
'44535',
'148468',
'135959',
'107084',
'166507',
'144191',
'281622',
'127006',
'104156',
'63060',
'33289',
'177465',
'369899',
'317979',
'111573',
'102815',
'322940',
'168173',
'300243',
'96598',
'113070',
'368333',
'78671',
'225192',
'369894',
'49517',
'22950',
'85869',
'62976',
'144301',
'297636',
'208767',
'247873',
'348707',
'270273',
'270781',
'54318',
'66205',
'313902',
'141523',
'303553',
'300145',
'244311',
'4236',
'77173',
'70413',
'49314',
'211055',
'320812',
'232545',
'129580',
'207637',
'363337',
'77075',
'148917',
'74668',
'159868',
'292558',
'144327',
'60905',
'103031',
'12263',
'334148',
'60069',
'140599',
'201808',
'316637',
'51008',
'319257',
'267304',
'180018',
'211104',
'299546',
'162241',
'147204',
'210566',
'358607',
'228792',
'347361',
'328244',
'191479',
'136693',
'171958',
'228766',
'367579',
'315306',
'194565',
'166402',
'40031',
'353098',
'283570',
'135183',
'115922',
'147854',
'28007',
'213165',
'110593',
'312285',
'224533',
'82031',
'178007',
'354302',
'107341',
'237779',
'183906',
'58814',
'275984',
'365021',
'133693',
'55319',
'346110',
'6959',
'30433',
'182546',
'154001',
'348560',
'201265',
'244085',
'295085',
'337732',
'250170',
'235728',
'110446',
'319829',
'89131',
'105764',
'129847',
'223344',
'140551',
'298063',
'62939',
'18072',
'296946',
'210541',
'303790',
'113864',
'329019',
'137272',
'163069',
'193469',
'265431',
'263265',
'119354',
'21253',
'117034',
'2055',
'110417',
'82234',
'133913',
'198144',
'162988',
'212670',
'287607',
'162284',
'28378',
'111827',
'354197',
'327300',
'198781',
'85952',
'304956',
'194945',
'190400',
'205093',
'193389',
'256164',
'34718',
'309423',
'32906',
'118371',
'299113',
'194601',
'240462',
'256133',
'281468',
'295140',
'238166',
'222445',
'144460',
'60470',
'162051',
'267256',
'25243',
'90307',
'259869',
'156606',
'269414',
'260071',
'307102',
'116220',
'102681',
'116429',
'231183',
'200556',
'256112',
'84666',
'49459',
'237485',
'141641',
'156782',
'204371',
'251598',
'198700',
'175753',
'279744',
'221066',
'144199',
'190484',
'198663',
'184172',
'35699',
'150272',
'1076',
'159208',
'222281',
'242334',
'330136',
'240862',
'164060',
'10846',
'126018',
'306456',
'9148',
'143559',
'216929',
'277156',
'83010',
'95085',
'45908',
'109855',
'368358',
'234777',
'41246',
'186249',
'250462',
'37390',
'249115',
'15910',
'50017',
'236459',
'156334',
'362063',
'37691',
'12559',
'316739',
'104549',
'15320',
'137009',
'17684',
'101986',
'295714',
'331057',
'13857',
'302028',
'114199',
'118252',
'243881',
'164341',
'311843',
'271686',
'150277',
'10953',
'268490',
'130667',
'209735',
'112343',
'363270',
'302998',
'169240',
'296097',
'217201',
'10511',
'178339',
'272811',
'125061',
'173808',
'286746',
'225040',
'275556',
'75712',
'220640',
'66621',
'113399',
'148905',
'78687',
'112077',
'227551',
'252336',
'152637',
'25394',
'367776',
'112151',
'12045',
'203758',
'321285',
'107061',
'52730',
'280042',
'369348',
'167538',
'284076',
'33629',
'177935',
'128106',
'325268',
'37069',
'195971',
'247777',
'11307',
'254348',
'203211',
'362563',
'281277',
'11786',
'101164',
'241324',
'350257',
'346237',
'359486',
'98192',
'132538',
'255556',
'226105',
'42495',
'214294',
'87241',
'39973',
'78238',
'219513',
'362470',
'218127',
'193758',
'242021',
'22992',
'14088',
'75212',
'134747',
'113724',
'184669',
'70244',
'253905',
'172236',
'52250',
'72524',
'197124',
'281466',
'274386',
'345696',
'64738',
'216404',
'130623',
'99870',
'85708',
'47471',
'195196',
'149450',
'76224',
'169842',
'197875',
'76311',
'172027',
'132408',
'301429',
'217300',
'104662',
'358571',
'288563',
'304112',
'218729',
'80923',
'349078',
'285017',
'163243',
'284580',
'367466',
'364965',
'179437',
'339863',
'309509',
'173090',
'41316',
'191306',
'129415',
'95481',
'159094',
'274559',
'148087',
'99517',
'171133',
'265042',
'294868',
'20818',
'13242',
'332575',
'50291',
'25494',
'24905',
'156676',
'125237',
'223594',
'124312',
'338256',
'95068',
'133238',
'190537',
'313772',
'71429',
'368096',
'22793',
'349699',
'222721',
'130888',
'96209',
'80866',
'333044',
'326891',
'249973',
'276814',
'240581',
'317859',
'275993',
'267076',
'28626',
'101712',
'144450',
'115211',
'120344',
'227096',
'368906',
'246711',
'199272',
'287896',
'184395',
'77378',
'270567',
'71772',
'70436',
'278446',
'249801',
'210984',
'128013',
'159337',
'336802',
'104572',
'182295',
'148318',
'339992',
'165636',
'215476',
'253417',
'357185',
'262244',
'182212',
'297667',
'73691',
'326844',
'13055',
'214129',
'93116',
'295462',
'40427',
'287569',
'94155',
'150719',
'237449',
'87417',
'101967',
'326035',
'336054',
'193573',
'4794',
'185930',
'136583',
'198471',
'183798',
'255221',
'95362',
'113251',
'193788',
'173835',
'17383',
'134648',
'335071',
'79100',
'202225',
'143782',
'99208',
'202678',
'44825',
'283894',
'123175',
'82363',
'226823',
'289395',
'59046',
'294408',
'256838',
'192605',
'48412',
'236403',
'223933',
'83563',
'20591',
'95742',
'79859',
'125211',
'50013',
'362730',
'284276',
'5460',
'27203',
'285736',
'220459',
'255560',
'275803',
'63687',
'177040',
'80545',
'306265',
'4494',
'323044',
'255311',
'356675',
'133007',
'284125',
'51102',
'37460',
'230880',
'273747',
'62924',
'265552',
'125932',
'313540',
'263511',
'29677',
'140077',
'307210',
'104469',
'272244',
'135355',
'126176',
'287048',
'173736',
'314964',
'19449',
'135006',
'30963',
'316937',
'134415',
'48946',
'177032',
'359432',
'210860',
'317855',
'253720',
'191888',
'271028',
'254216',
'326353',
'340618',
'35864',
'55281',
'274429',
'279101',
'2819',
'295215',
'135427',
'144660',
'298493',
'270319',
'306929',
'58834',
'366428',
'69635',
'33921',
'363413',
'208703',
'351347',
'138017',
'5371',
'349482',
'283196',
'156071',
'312333',
'155022',
'270688',
'50667',
'192482',
'10797',
'305005',
'267952',
'12885',
'342533',
'199683',
'8003',
'55585',
'238448',
'8207',
'130108',
'159698',
'134189',
'7141',
'77548',
'134787',
'159975',
'240146',
'331268',
'57929',
'312630',
'212817',
'198025',
'98673',
'242240',
'49748',
'332977',
'328372',
'307698',
'15468',
'296961',
'309885',
'103516',
'67731',
'52357',
'94466',
'215894',
'141316',
'298487',
'320903',
'18808',
'220884',
'285570',
'268761',
'232035',
'279682',
'343723',
'177534',
'321100',
'222477',
'306286',
'220528',
'221512',
'201124',
'287480',
'48975',
'213351',
'108534',
'23961',
'200287',
'44432',
'301451',
'82668',
'284415',
'293539',
'201392',
'112839',
'274472',
'81606',
'329333',
'107897',
'41225',
'221664',
'107051',
'202947',
'347352',
'287704',
'131893',
'201616',
'56994',
'28736',
'285191',
'9939',
'223151',
'96259',
'347716',
'272876',
'58534',
'45095',
'318052',
'93660',
'90743',
'47082',
'206808',
'77494',
'138637',
'175720',
'357726',
'116620',
'353201',
'255114',
'347905',
'188609',
'357032',
'20610',
'251816',
'251833',
'46222',
'194764',
'336905',
'263934',
'355134',
'243524',
'198621',
'207957',
'51300',
'85187',
'181805',
'267783',
'115861',
'37419',
'352329',
'18385',
'76551',
'284454',
'143651',
'214867',
'23362',
'229669',
'322483',
'11532',
'361449',
'98128',
'131580',
'121750',
'128036',
'239985',
'127576',
'107598',
'3231',
'49615',
'171080',
'9947',
'94310',
'242337',
'54385',
'151972',
'79490',
'157323',
'240879',
'364527',
'345587',
'228347',
'88177',
'326293',
'348977',
'230263',
'13047',
'53323',
'322286',
'171826',
'362568',
'168467',
'41619',
'275343',
'185539',
'311465',
'131642',
'279898',
'325446',
'153980',
'93566',
'339536',
'55443',
'256861',
'211235',
'284618',
'53816',
'180732',
'155005',
'325704',
'209108',
'108278',
'91373',
'194703',
'76263',
'107904',
'227571',
'102677',
'40774',
'366894',
'32022',
'162309',
'242150',
'299984',
'231708',
'335313',
'83402',
'148488',
'34038',
'157922',
'103262',
'281952',
'192244',
'13901',
'32792',
'363013',
'5336',
'83236',
'161885',
'90370',
'305410',
'21693',
'205228',
'283319',
'82816',
'346034',
'74749',
'341372',
'288782',
'142111',
'279900',
'206115',
'282978',
'308504',
'167537',
'230962',
'46177',
'155813',
'334029',
'314450',
'20706',
'274871',
'357949',
'346758',
'150991',
'306969',
'554',
'30591',
'70215',
'128115',
'363632',
'268875',
'26105',
'71277',
'60802',
'58027',
'38946',
'273855',
'351340',
'162586',
'149339',
'129366',
'118242',
'237062',
'218499',
'103342',
'130254',
'335458',
'294811',
'144980',
'215748',
'210177',
'333711',
'340278',
'228125',
'328925',
'325079',
'196147',
'261491',
'236781',
'104611',
'50311',
'151691',
'312202',
'189121',
'104432',
'198735',
'13882',
'286207',
'84357',
'164914',
'71359',
'212467',
'351721',
'125379',
'279384',
'62998',
'216807',
'311623',
'184952',
'17166',
'139640',
'324272',
'350129',
'262222',
'101229',
'120503',
'173283',
'21542',
'37833',
'4090',
'351599',
'263480',
'8055',
'347336',
'300519',
'281280',
'321406',
'150798',
'254199',
'114369',
'351913',
'50250',
'71916',
'32831',
'250479',
'45629',
'86243',
'205905',
'363931',
'223886',
'277635',
'146010',
'200412',
'56913',
'36476',
'306866',
'174208',
'242368',
'223944',
'99287',
'357057',
'220997',
'232761',
'59278',
'124237',
'237252',
'189673',
'295629',
'18284',
'114089',
'288964',
'117291',
'119571',
'129467',
'237707',
'251641',
'7278',
'268605',
'267351',
'170676',
'291203',
'346103',
'239833',
'321974',
'267476',
'263311',
'31725',
'38925',
'350427',
'206990',
'257433',
'332449',
'107703',
'276565',
'260791',
'209575',
'127345',
'321872',
'206204',
'309762',
'176523',
'114965',
'200283',
'319110',
'162768',
'123230',
'63311',
'362668',
'215019',
'152091',
'105401',
'179574',
'104214',
'31840',
'95746',
'237715',
'104052',
'997',
'115433',
'30063',
'120750',
'319254',
'180876',
'50304',
'108961',
'72402',
'60449',
'230076',
'261731',
'38111',
'15677',
'168705',
'322965',
'85028',
'288047',
'97205',
'264227',
'83081',
'274543',
'243808',
'222081',
'98887',
'136931',
'235095',
'349333',
'370044',
'287945',
'177036',
'84468',
'123107',
'15578',
'44525',
'220007',
'11455',
'259937',
'298531',
'345112',
'304791',
'306535',
'104237',
'207067',
'144764',
'179759',
'110174',
'31089',
'168862',
'1685',
'47014',
'152729',
'104824',
'145979',
'9886',
'48850',
'350353',
'304091',
'114413',
'174947',
'14725',
'309837',
'87600',
'290011',
'85152',
'233206',
'195457',
'93504',
'227306',
'103762',
'280305',
'253898',
'346501',
'221648',
'332713',
'313213',
'251672',
'167303',
'272803',
'17445',
'196143',
'30279',
'4875',
'344715',
'3173',
'240018',
'21290',
'166504',
'42441',
'262529',
'346241',
'54570',
'146985',
'338554',
'10687',
'193500',
'192043',
'352868',
'151525',
'57130',
'304507',
'121009',
'120724',
'41762',
'61564',
'247906',
'95594',
'178414',
'277950',
'36979',
'362575',
'97893',
'116949',
'130973',
'119771',
'238480',
'347108',
'9625',
'208825',
'97039',
'88489',
'144438',
'238218',
'313722',
'166710',
'357326',
'175547',
'285528',
'229609',
'112319',
'359488',
'240756',
'103568',
'196322',
'358545',
'228232',
'338804',
'224603',
'357822',
'7824',
'352684',
'317094',
'35466',
'317085',
'167864',
'353013',
'119791',
'101336',
'283736',
'50278',
'364250',
'218183',
'275982',
'56195',
'78060',
'300826',
'114047',
'366009',
'292695',
'122573',
'123524',
'311346',
'365534',
'183659',
'218294',
'33536',
'130490',
'346877',
'357661',
'95241',
'196582',
'230736',
'356114',
'338169',
'247451',
'6586',
'339703',
'7312',
'148205',
'297058',
'183997',
'306743',
'267528',
'347462',
'59289',
'138024',
'40275',
'170123',
'12665',
'8685',
'34800',
'115263',
'80524',
'84627',
'338351',
'361121',
'82550',
'188894',
'329387',
'229783',
'324997',
'364597',
'265565',
'156176',
'340577',
'155686',
'45362',
'250472',
'219868',
'260769',
'199886',
'337826',
'318740',
'118881',
'14216',
'68721',
'292591',
'77492',
'129925',
'167106',
'310224',
'199085',
'110205',
'128469',
'102896',
'368449',
'278541',
'280045',
'126488',
'1936',
'261478',
'94735',
'304388',
'230408',
'33150',
'206498',
'297698',
'168825',
'325423',
'145703',
'17631',
'86441',
'54978',
'338737',
'58590',
'6017',
'173961',
'226653',
'345739',
'253271',
'93979',
'245786',
'275783',
'223558',
'216553',
'358270',
'333105',
'70313',
'209796',
'245982',
'170209',
'115045',
'16809',
'222503',
'93512',
'245535',
'324630',
'294739',
'215141',
'127471',
'27331',
'101606',
'182418',
'123251',
'215706',
'362491',
'189162',
'156011',
'161911',
'15612',
'191598',
'346400',
'122826',
'353692',
'274426',
'183556',
'332071',
'185721',
'5519',
'84452',
'170679',
'339184',
'327468',
'366010',
'5646',
'49026',
'41890',
'148958',
'77001',
'101103',
'54898',
'107378',
'99244',
'72799',
'324736',
'161326',
'14400',
'5449',
'51777',
'276799',
'241664',
'186217',
'30046',
'152834',
'62047',
'191251',
'76448',
'200230',
'221347',
'6464',
'93824',
'289019',
'26437',
'259006',
'105167',
'181301',
'178013',
'240413',
'192424',
'15303',
'46811',
'12663',
'326886',
'205956',
'162494',
'137575',
'160860',
'26201',
'364114',
'112062',
'6174',
'215546',
'103044',
'97215',
'256261',
'279314',
'356482',
'229981',
'79754',
'134733',
'94671',
'206560',
'205393',
'223542',
'101785',
'366746',
'160002',
'274992',
'47955',
'342919',
'219484',
'218702',
'25224',
'207385',
'14784',
'208669',
'112883',
'220448',
'6684',
'186211',
'273084',
'341159',
'147823',
'79445',
'55992',
'344175',
'261188',
'132302',
'97874',
'351354',
'228233',
'34526',
'71489',
'249045',
'46971',
'318199',
'192470',
'100933',
'147809',
'27894',
'243872',
'326657',
'10835',
'361604',
'45182',
'187842',
'3195',
'67968',
'297964',
'339989',
'262216',
'126489',
'140209',
'10305',
'53874',
'257254',
'7878',
'228680',
'356446',
'21010',
'10430',
'259973',
'125962',
'239723',
'2251',
'112531',
'341645',
'56655',
'221699',
'367398',
'342778',
'199766',
'146570',
'344457',
'125343',
'121634',
'6680',
'239707',
'151259',
'268326',
'157956',
'531',
'321831',
'121695',
'259726',
'333698',
'15414',
'153292',
'319266',
'171731',
'264197',
'45834',
'150134',
'359505',
'106278',
'9094',
'363070',
'56637',
'136052',
'126283',
'10526',
'352958',
'88920',
'152983',
'37683',
'341427',
'218536',
'264916',
'186795',
'11234',
'190219',
'259513',
'153571',
'292781',
'149977',
'304654',
'362492',
'82422',
'194742',
'111406',
'274775',
'180691',
'344849',
'270790',
'283564',
'120984',
'340597',
'283154',
'255037',
'224102',
'300367',
'352438',
'69454',
'195429',
'300150',
'40605',
'23580',
'38935',
'76324',
'250239',
'179564',
'185346',
'335534',
'238245',
'100246',
'124639',
'353755',
'239232',
'363991',
'160478',
'174356',
'62227',
'201180',
'175189',
'289890',
'274604',
'340325',
'238018',
'212923',
'199634',
'139577',
'25920',
'329044',
'341087',
'138464',
'332355',
'294426',
'167285',
'2404',
'277410',
'132987',
'355564',
'182050',
'26838',
'355643',
'41208',
'230234',
'26390',
'18510',
'155831',
'326635',
'165136',
'202056',
'228231',
'9615',
'220965',
'272109',
'320319',
'3028',
'195518',
'39796',
'43277',
'94725',
'278492',
'78545',
'141117',
'191361',
'207104',
'214868',
'161158',
'283250',
'212196',
'86176',
'367320',
'334374',
'255640',
'107117',
'149850',
'25439',
'160331',
'74551',
'212274',
'366974',
'238617',
'85530',
'103834',
'222169',
'112751',
'195416',
'320608',
'216860',
'193330',
'44547',
'167882',
'256179',
'171569',
'149446',
'321249',
'126581',
'34664',
'72154',
'335844',
'132356',
'216523',
'18032',
'129932',
'154808',
'40123',
'2943',
'42446',
'229681',
'110690',
'15309',
'90636',
'104999',
'116211',
'266414',
'21204',
'150205',
'166216',
'230058',
'193652',
'341643',
'39939',
'258569',
'154362',
'124743',
'345223',
'209157',
'131121',
'17864',
'114005',
'226534',
'772',
'179526',
'186118',
'252500',
'7079',
'244332',
'270075',
'239761',
'307561',
'193292',
'41298',
'252211',
'47615',
'319838',
'360991',
'197859',
'82416',
'358934',
'148493',
'242785',
'61024',
'77834',
'309666',
'265286',
'265039',
'267201',
'52307',
'95850',
'122531',
'297520',
'25776',
'87561',
'96591',
'363787',
'172134',
'246064',
'252766',
'342559',
'367100',
'160718',
'192677',
'24981',
'211018',
'29852',
'282007',
'50645',
'84466',
'8321',
'37183',
'208340',
'321352',
'264289',
'311296',
'216166',
'298805',
'271882',
'310961',
'164222',
'3901',
'142472',
'340446',
'222597',
'145164',
'97637',
'107306',
'289711',
'268991',
'161769',
'62494',
'307716',
'190574',
'251266',
'55541',
'40628',
'323232',
'10857',
'103555',
'4116',
'86184',
'30419',
'210987',
'245894',
'181114',
'184226',
'369970',
'336050',
'337992',
'69865',
'256722',
'9848',
'336231',
'79269',
'230739',
'283822',
'153681',
'194980',
'163686',
'296318',
'275171',
'205086',
'293263',
'151956',
'85612',
'325524',
'304591',
'252545',
'130950',
'196309',
'95281',
'19860',
'76938',
'134242',
'252355',
'69713',
'283451',
'172945',
'140518',
'274274',
'168075',
'136360',
'204520',
'299988',
'158530',
'106436',
'310919',
'298758',
'22412',
'136615',
'213715',
'238697',
'213296',
'362490',
'93346',
'271669',
'20643',
'213325',
'280012',
'186882',
'306414',
'49260',
'248478',
'115824',
'175132',
'116348',
'175151',
'62279',
'233331',
'276549',
'186898',
'121590',
'367970',
'261652'
)
limit 7000;
