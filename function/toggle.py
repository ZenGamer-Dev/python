--[[
 .____                  ________ ___.    _____                           __                
 |    |    __ _______   \_____  \\_ |___/ ____\_ __  ______ ____ _____ _/  |_  ___________ 
 |    |   |  |  \__  \   /   |   \| __ \   __\  |  \/  ___// ___\\__  \\   __\/  _ \_  __ \
 |    |___|  |  // __ \_/    |    \ \_\ \  | |  |  /\___ \\  \___ / __ \|  | (  <_> )  | \/
 |_______ \____/(____  /\_______  /___  /__| |____//____  >\___  >____  /__|  \____/|__|   
         \/          \/         \/    \/                \/     \/     \/                   
          \_Welcome to LuaObfuscator.com   (Alpha 0.10.8) ~  Much Love, Ferib 

]]--

local v0=tonumber;local v1=string.byte;local v2=string.char;local v3=string.sub;local v4=string.gsub;local v5=string.rep;local v6=table.concat;local v7=table.insert;local v8=math.ldexp;local v9=getfenv or function() return _ENV;end ;local v10=setmetatable;local v11=pcall;local v12=select;local v13=unpack or table.unpack ;local v14=tonumber;local function v15(v16,v17,...) local v18=1;local v19;v16=v4(v3(v16,5),"..",function(v30) if (v1(v30,2)==81) then local v79=0;while true do if (v79==0) then v19=v0(v3(v30,1,1));return "";end end else local v80=0;local v81;while true do if (v80==0) then v81=v2(v0(v30,16));if v19 then local v105=0;local v106;while true do if (v105==1) then return v106;end if (v105==0) then v106=v5(v81,v19);v19=nil;v105=1;end end else return v81;end break;end end end end);local function v20(v31,v32,v33) if v33 then local v82=(v31/((5 -3)^(v32-(2 -1))))%(2^(((v33-(1 -0)) -(v32-1)) + (2 -1))) ;return v82-(v82%1) ;else local v83=619 -((1432 -(282 + 595)) + 64) ;local v84;while true do if (v83==(931 -(857 + 74))) then v84=(570 -(367 + 201))^(v32-((2565 -(1523 + 114)) -(214 + 713))) ;return (((v31%(v84 + v84))>=v84) and (1 + 0)) or (0 + 0) ;end end end end local function v21() local v34=v1(v16,v18,v18);v18=v18 + 1 ;return v34;end local function v22() local v35,v36=v1(v16,v18,v18 + 2 + 0 );v18=v18 + 2 ;return (v36 * (364 -108)) + v35 ;end local function v23() local v37,v38,v39,v40=v1(v16,v18,v18 + (1068 -(68 + 222 + 775)) );v18=v18 + (1274 -(226 + 1044)) ;return (v40 * (73054774 -56277558)) + (v39 * (65653 -((989 -(892 + 65)) + 85))) + (v38 * (251 + 5)) + v37 ;end local function v24() local v41=v23();local v42=v23();local v43=(1189 -(1069 + 118)) -1 ;local v44=(v20(v42,1 -0 ,36 -16 ) * ((352 -(87 + (596 -333)))^(212 -(67 + 113)))) + v41 ;local v45=v20(v42,21,31);local v46=((v20(v42,24 + 8 )==1) and  -(2 -(1 -0))) or (1 + 0) ;if (v45==(0 -0)) then if (v44==(952 -(802 + 27 + 123))) then return v46 * 0 ;else v45=1;v43=0 -0 ;end elseif (v45==((6595 -2883) -1665)) then return ((v44==(0 + 0)) and (v46 * ((998 -(908 + 7 + 82))/((791 -(368 + 423)) -0)))) or (v46 * NaN) ;end return v8(v46,v45-(596 + 427) ) * (v43 + (v44/(2^(68 -16)))) ;end local function v25(v47) local v48=(430 -(44 + 386)) -0 ;local v49;local v50;while true do if (v48==2) then v50={};for v92=19 -(10 + 8) , #v49 do v50[v92]=v2(v1(v3(v49,v92,v92)));end v48=11 -8 ;end if (v48==(443 -(416 + 26))) then v49=v3(v16,v18,(v18 + v47) -(3 -(1488 -(998 + 488))) );v18=v18 + v47 ;v48=2;end if (v48==(2 + 1 + 0)) then return v6(v50);end if (v48==(0 -0)) then v49=nil;if  not v47 then v47=v23();if (v47==0) then return "";end end v48=439 -(145 + 293) ;end end end local v26=v23;local function v27(...) return {...},v12("#",...);end local function v28() local v51=(function() return 1194 -(352 + 842) ;end)();local v52=(function() return;end)();local v53=(function() return;end)();local v54=(function() return;end)();local v55=(function() return;end)();local v56=(function() return;end)();local v57=(function() return;end)();local v58=(function() return;end)();while true do if (v51==1) then v55=(function() return {};end)();v56=(function() return {v53,v54,nil,v55};end)();v57=(function() return v23();end)();v51=(function() return 2 + 0 ;end)();end if (v51==0) then local v88=(function() return 0;end)();local v89=(function() return;end)();while true do if (v88==(1821 -(1483 + 338))) then v89=(function() return 0 -0 ;end)();while true do if (v89==(1696 -(1229 + 466))) then v54=(function() return {};end)();v51=(function() return 579 -(386 + 192) ;end)();break;end if (v89~=(1206 -(696 + 510))) then else v52=(function() return function(v116,v117,v118) local v119=(function() return 867 -(550 + 317) ;end)();local v120=(function() return;end)();while true do if (v119==(0 -0)) then v120=(function() return 0;end)();while true do if ((0 -0)~=v120) then else v116[v117-#"," ]=(function() return v118();end)();return v116,v117,v118;end end break;end end end;end)();v53=(function() return {};end)();v89=(function() return 1263 -(1091 + 171) ;end)();end end break;end end end if (v51==3) then for v94= #"[",v23() do local v95=(function() return v21();end)();if (v20(v95, #"}", #">")~=0) then else local v101=(function() return 0;end)();local v102=(function() return;end)();local v103=(function() return;end)();local v104=(function() return;end)();while true do if (v101~=(1 + 2)) then else if (v20(v103, #"-19", #"xnx")== #"\\") then v104[ #".dev"]=(function() return v58[v104[ #"?id="]];end)();end v53[v94]=(function() return v104;end)();break;end if (v101==0) then local v108=(function() return 0 -0 ;end)();local v109=(function() return;end)();while true do if ((285 -(134 + 151))==v108) then v109=(function() return 0;end)();while true do if ((0 -0)~=v109) then else v102=(function() return v20(v95,3 -1 , #"19(");end)();v103=(function() return v20(v95, #"asd1",6);end)();v109=(function() return 3 -2 ;end)();end if (v109==(375 -(123 + 251))) then v101=(function() return 1;end)();break;end end break;end end end if (v101==1) then local v110=(function() return 0 -0 ;end)();while true do if (v110==(699 -(208 + 490))) then v101=(function() return 2;end)();break;end if (v110==0) then v104=(function() return {v22(),v22(),nil,nil};end)();if (v102==(0 -0)) then local v125=(function() return 0 + 0 ;end)();local v126=(function() return;end)();while true do if (v125==(0 -0)) then v126=(function() return 836 -(660 + 176) ;end)();while true do if (v126~=(0 + 0)) then else v104[ #"asd"]=(function() return v22();end)();v104[ #"0313"]=(function() return v22();end)();break;end end break;end end elseif (v102== #"{") then v104[ #"91("]=(function() return v23();end)();elseif (v102==(2 -0)) then v104[ #"asd"]=(function() return v23() -((243 -(187 + 54))^(796 -(162 + 618))) ;end)();elseif (v102~= #"19(") then else local v352=(function() return 202 -(14 + 188) ;end)();while true do if (v352==0) then v104[ #"asd"]=(function() return v23() -(2^(12 + 4)) ;end)();v104[ #"?id="]=(function() return v22();end)();break;end end end v110=(function() return 676 -(534 + 141) ;end)();end end end if (v101~=2) then else if (v20(v103, #"|", #"[")== #"!") then v104[1 + 1 ]=(function() return v58[v104[2]];end)();end if (v20(v103,3 -1 ,2 + 0 )== #"[") then v104[ #"91("]=(function() return v58[v104[ #"xxx"]];end)();end v101=(function() return 3;end)();end end end end for v96= #"~",v23() do v54,v96,v28=(function() return v52(v54,v96,v28);end)();end return v56;end if (v51==(1 + 1)) then local v90=(function() return 1636 -(1373 + 263) ;end)();local v91=(function() return;end)();while true do if (v90==(0 + 0)) then v91=(function() return 0 -0 ;end)();while true do if (v91~=(1 -0)) then else v56[ #"nil"]=(function() return v21();end)();v51=(function() return 4 -1 ;end)();break;end if (v91==0) then v58=(function() return {};end)();for v112= #"!",v57 do local v113=(function() return 0 -0 ;end)();local v114=(function() return;end)();local v115=(function() return;end)();while true do if ((0 + 0)~=v113) then else v114=(function() return v21();end)();v115=(function() return nil;end)();v113=(function() return 1;end)();end if (v113~=(1 -0)) then else if (v114== #"!") then v115=(function() return v21()~=(0 + 0) ;end)();elseif (v114==(398 -(115 + 281))) then v115=(function() return v24();end)();elseif (v114== #"xnx") then v115=(function() return v25();end)();end v58[v112]=(function() return v115;end)();break;end end end v91=(function() return 1;end)();end end break;end end end end end local function v29(v59,v60,v61) local v62=v59[1 + 0 ];local v63=v59[2 -0 ];local v64=v59[3];return function(...) local v65=v62;local v66=v63;local v67=v64;local v68=v27;local v69=342 -(218 + 123) ;local v70= -(1582 -(1535 + 46));local v71={};local v72={...};local v73=v12("#",...) -((1035 -(125 + 909)) + 0) ;local v74={};local v75={};for v85=560 -((2254 -(1096 + 852)) + 254) ,v73 do if (v85>=v67) then v71[v85-v67 ]=v72[v85 + 1 + 0 + 0 ];else v75[v85]=v72[v85 + (1 -0) ];end end local v76=(v73-v67) + (1468 -(899 + 568)) ;local v77;local v78;while true do v77=v65[v69];v78=v77[1 + 0 ];if ((1612==1612) and (v78<=(60 -17))) then if (v78<=(50 -29)) then if (v78<=(613 -(268 + 335))) then if ((2981==2981) and (v78<=(294 -(60 + 230)))) then if (v78<=(573 -(426 + 146))) then if (v78==(0 + 0)) then local v127=v77[1458 -(282 + 1174) ];local v128={};for v185=(788 + 24) -((1081 -(409 + 103)) + 242) , #v74 do local v186=v74[v185];for v194=0 -0 , #v186 do local v195=v186[v194];local v196=v195[1 + 0 ];local v197=v195[2];if ((4352>=2833) and (493==493) and (v196==v75) and (v197>=v127)) then local v303=1024 -(706 + 318) ;while true do if (v303==(1251 -(721 + (766 -(46 + 190))))) then v128[v197]=v196[v197];v195[1272 -(945 + 326) ]=v128;break;end end end end end else v75[v77[(99 -(51 + 44)) -2 ]]=v75[v77[3 + 0 ]] + v75[v77[704 -(271 + 429) ]] ;end elseif ((v78<=(2 + 0)) or (2467==1987) or (3222<3073)) then v75[v77[1502 -(1408 + 92) ]]=v75[v77[1089 -(461 + 625) ]];elseif (v78>(1291 -(993 + 295))) then v75[v77[1 + 1 ]]=v77[1174 -(418 + 213 + 540) ] + v75[v77[2 + 2 ]] ;else local v199=0 + 0 ;local v200;local v201;while true do if ((744<=2942) and ((v199==((1317 -(1114 + 203)) + 0)) or (1205>1333))) then v200=v77[2];v201=v75[v77[3]];v199=(727 -(228 + 498)) + 0 ;end if ((v199==1) or (3696<=3327) or (1833<=1322)) then v75[v200 + (530 -(406 + 123)) ]=v201;v75[v200]=v201[v77[1773 -(1749 + 20) ]];break;end end end elseif (v78<=(2 + 5)) then if (v78<=(1327 -(1249 + 73))) then v75[v77[1 + 1 ]]=v61[v77[(249 + 899) -(466 + 679) ]];elseif ((v78==(14 -(5 + 3))) or (4542==2970)) then local v202=v77[(668 -(174 + 489)) -3 ];v75[v202](v75[v202 + (1901 -(106 + 1794)) ]);else local v203=0 + 0 ;local v204;while true do if ((v203==(0 + 0)) or (3467<=1055)) then v204=v77[(12 -7) -3 ];v75[v204](v13(v75,v204 + (2 -1) ,v70));break;end end end elseif (v78<=(122 -(4 + 110))) then v75[v77[2]]=v75[v77[3]] + v77[588 -(57 + 527) ] ;elseif (v78==9) then v75[v77[1429 -(41 + 1386) ]]=v75[v77[3]][v77[(2012 -(830 + 1075)) -((541 -(303 + 221)) + 86) ]];else v75[v77[2 + 0 ]]=v77[6 -3 ]~=(0 -0) ;end elseif (v78<=15) then if ((3541==3541) and (v78<=12)) then if (((252<=1977) and (v78>(177 -(122 + 44)))) or (3557>=4003)) then if ((v75[v77[2 -0 ]]==v77[(1281 -(231 + 1038)) -8 ]) or (657>=1668)) then v69=v69 + 1 + 0 ;else v69=v77[3 + 0 ];end else local v135=v77[1 + 1 ];local v136=v75[v135 + (3 -(1163 -(171 + 991))) ];local v137=v75[v135] + v136 ;v75[v135]=v137;if (v136>(65 -(30 + 35))) then if (v137<=v75[v135 + 1 + 0 ]) then v69=v77[1260 -(1043 + 214) ];v75[v135 + (11 -(32 -24)) ]=v137;end elseif ((v137>=v75[v135 + (1213 -(323 + 889)) ]) or (1027>3858)) then local v306=0 -0 ;while true do if (v306==(580 -(361 + 219))) then v69=v77[323 -(53 + 267) ];v75[v135 + 3 ]=v137;break;end end end end elseif (v78<=(3 + 10)) then v75[v77[415 -(15 + 398) ]]={};elseif ((v78==((2674 -1678) -((44 -26) + 964))) or (1436==3775)) then v69=v77[11 -8 ];else for v285=v77[2],v77[2 + 1 ] do v75[v285]=nil;end end elseif ((v78<=18) or (3654<450)) then if (v78<=(11 + 5)) then v75[v77[852 -(20 + 665 + 165) ]]=v61[v77[(10 -7) + 0 ]];elseif (v78>(143 -(116 + (28 -18)))) then v75[v77[1 + 1 ]]=v75[v77[741 -(542 + 196) ]][v77[8 -4 ]];else v75[v77[1 + 1 ]]=v77[2 + 1 ];end elseif ((1891<4453) and ((v78<=((10 -3) + 12)) or (1618<930))) then do return;end elseif (v78>(52 -32)) then local v214=v77[(12 -8) -2 ];local v215,v216=v68(v75[v214](v13(v75,v214 + (1552 -(1126 + 425)) ,v77[408 -(118 + 287) ])));v70=(v216 + v214) -1 ;local v217=0 -0 ;for v287=v214,v70 do v217=v217 + (1122 -(118 + 1003)) ;v75[v287]=v215[v217];end elseif (v75[v77[5 -3 ]]==v75[v77[381 -(142 + 235) ]]) then v69=v69 + (4 -3) ;else v69=v77[1 + 2 ];end elseif ((4723>4153) and (v78<=(1009 -(553 + 424)))) then if (v78<=26) then if ((v78<=((1290 -(111 + 1137)) -19)) or (3654>=4654)) then if (v78>(20 + 2)) then local v142=v77[(160 -(91 + 67)) + 0 ];local v143=v75[v142];local v144=v75[v142 + 2 + 0 ];if ((v144>(0 + 0)) or (3140<2129)) then if ((951<=1496) and (v143>v75[v142 + 1 + 0 ])) then v69=v77[3];else v75[v142 + (6 -3) ]=v143;end elseif ((v143<v75[v142 + (2 -1) ]) or (2555<1240)) then v69=v77[6 -3 ];else v75[v142 + (2 -1) + 2 ]=v143;end else local v145=v77[(3 + 6) -7 ];v75[v145](v13(v75,v145 + 1 ,v70));end elseif (v78<=(777 -((762 -(423 + 100)) + 514))) then local v146=0 + 0 ;local v147;local v148;local v149;local v150;while true do if (v146==(1330 -(6 + 791 + 532))) then v70=(v149 + v147) -(1 + 0) ;v150=(0 -0) + 0 ;v146=2;end if ((v146==(4 -(2 + 0))) or (4727<=4722)) then for v312=v147,v70 do local v313=1202 -(373 + 829) ;while true do if (v313==((1502 -(326 + 445)) -(476 + 255))) then v150=v150 + 1 ;v75[v312]=v148[v150];break;end end end break;end if ((v146==(1130 -(369 + 761))) or (1736==571)) then v147=v77[2 + (0 -0) ];v148,v149=v68(v75[v147](v13(v75,v147 + (1 -0) ,v70)));v146=1 -0 ;end end elseif (v78==(263 -(64 + 174))) then v75[v77[2]]=v77[3]~=(0 + 0) ;else v75[v77[2 -0 ]]=v60[v77[339 -(144 + 192) ]];end elseif ((740<4937) and ((v78<=(245 -(42 + 174))) or (896>4769))) then if ((v78<=(21 + 6)) or (1045<=1020)) then local v151=v77[2 + 0 ];do return v75[v151](v13(v75,v151 + 1 ,v77[2 + 1 ]));end elseif (v78>((3412 -1880) -(363 + (2663 -1522)))) then if (v75[v77[2]] or (1160<=328)) then v69=v69 + 1 ;else v69=v77[1583 -(1183 + 397) ];end else local v221=0 -0 ;local v222;local v223;local v224;while true do if (v221==(1 + (711 -(530 + 181)))) then v224=v75[v222 + 2 ];if ((3658>=280) and (v224>(0 + 0))) then if (v223>v75[v222 + (1976 -((2794 -(614 + 267)) + (94 -(19 + 13)))) ]) then v69=v77[2 + 1 ];else v75[v222 + (7 -4) ]=v223;end elseif ((3808>2924) and (v223<v75[v222 + ((3147 -1213) -((1316 -751) + 1368)) ])) then v69=v77[11 -(22 -14) ];else v75[v222 + ((433 + 1231) -(1477 + 184)) ]=v223;end break;end if (((3891<4919) and (v221==(0 -0))) or (885>=1031)) then v222=v77[2 + 0 ];v223=v75[v222];v221=857 -(564 + 292) ;end end end elseif ((v78<=(52 -22)) or (2234<=1502)) then local v152=v77[2 -0 ];local v153,v154=v68(v75[v152](v13(v75,v152 + 1 ,v70)));v70=(v154 + v152) -((3 -1) -1) ;local v155=304 -(244 + (1872 -(1293 + 519))) ;for v187=v152,v70 do v155=v155 + 1 ;v75[v187]=v153[v155];end elseif (v78>31) then local v225=v77[2 + 0 ];v75[v225](v13(v75,v225 + (477 -(41 + 435)) ,v77[3]));else v75[v77[1003 -(938 + 63) ]][v77[3 + 0 ]]=v77[1129 -(936 + 189) ];end elseif (v78<=(13 + 24)) then if ((3554>=525) and ((v78<=((3359 -1712) -(1565 + 48))) or (2512<432))) then if (v78==(21 + 12)) then if ((v75[v77[1140 -(782 + 356) ]]==v75[v77[271 -(176 + 91) ]]) or (1848==865)) then v69=v69 + 1 ;else v69=v77[7 -4 ];end else v75[v77[2 -0 ]]=v75[v77[3]];end elseif (v78<=35) then do return;end elseif ((2414<=2972) and (v78==(1128 -(975 + 117)))) then v75[v77[1877 -((409 -252) + 1718) ]]=v75[v77[3 + 0 ]] -v75[v77[14 -10 ]] ;else local v230=v77[6 -4 ];local v231={};for v291=1019 -(697 + 321) , #v74 do local v292=v74[v291];for v315=0 -0 , #v292 do local v316=v292[v315];local v317=v316[1 -0 ];local v318=v316[4 -2 ];if ((3529<=3538) and (v317==v75) and (v318>=v230)) then v231[v318]=v317[v318];v316[1 + 0 ]=v231;end end end end elseif ((v78<=40) or (4682<=4541) or (2861<458)) then if ((1717<=4525) and (v78<=38)) then local v158=(0 -0) -(0 -0) ;local v159;while true do if ((v158==(0 -0)) or (3026>=4046) or (3178<=1524)) then v159=v77[1229 -(322 + 905) ];v75[v159]=v75[v159](v13(v75,v159 + (2 -1) ,v70));break;end end elseif ((2008>638) and (v78==((345 + 305) -(602 + 9)))) then for v295=v77[1191 -(449 + 151 + 589) ],v77[875 -((1918 -1092) + 46) ] do v75[v295]=nil;end else local v232=v77[949 -(245 + 702) ];local v233=v75[v232 + (6 -4) ];local v234=v75[v232] + v233 ;v75[v232]=v234;if (v233>0) then if ((1775<=3233) and (v234<=v75[v232 + 1 ])) then local v356=0 + 0 ;while true do if ((4254>370) and (v356==(1898 -(260 + 1638)))) then v69=v77[443 -(382 + 58) ];v75[v232 + ((3 + 6) -6) ]=v234;break;end end end elseif (v234>=v75[v232 + 1 + 0 + 0 ]) then v69=v77[5 -2 ];v75[v232 + (8 -5) ]=v234;end end elseif (v78<=41) then if ((v75[v77[1207 -(902 + 303) ]]~=v75[v77[8 -4 ]]) or (4543==1997)) then v69=v69 + (2 -1) ;else v69=v77[1 + 2 ];end elseif ((v78>(1732 -(1121 + 569))) or (3102<728)) then local v237=v77[2];do return v75[v237](v13(v75,v237 + (215 -(22 + 192)) ,v77[2 + 1 ]));end else v75[v77[685 -(483 + 200) ]]();end elseif (v78<=((2624 -(709 + 387)) -(1404 + 59))) then if ((v78<=54) or (1635==1777)) then if ((345==345) and (v78<=((1989 -(673 + 1185)) -(240 -157)))) then if ((v78<=(60 -15)) or (3338>=3993)) then if (v78==(140 -96)) then local v160=765 -((769 -301) + 297) ;local v161;local v162;local v163;while true do if (v160==(563 -(334 + 228))) then v163={};v162=v10({},{__index=function(v319,v320) local v321=0 -0 ;local v322;while true do if ((1154<=1475) and ((0 -0)==v321)) then v322=v163[v320];return v322[1 -0 ][v322[2]];end end end,__newindex=function(v323,v324,v325) local v326=0 + 0 ;local v327;while true do if (v326==(236 -(141 + 95))) then v327=v163[v324];v327[1 + 0 ][v327[4 -2 ]]=v325;break;end end end});v160=4 -2 ;end if (v160==(1 + 1)) then for v328=1,v77[4] do v69=v69 + (2 -1) ;local v329=v65[v69];if (v329[1]==(24 + 10)) then v163[v328-(1 + 0 + 0) ]={v75,v329[2 + 1 ]};else v163[v328-(164 -(92 + 71)) ]={v60,v329[768 -(574 + 191) ]};end v74[ #v74 + (1 -0) ]=v163;end v75[v77[2 + (0 -0) ]]=v29(v161,v162,v61);break;end if (v160==((1880 -(446 + 1434)) -0)) then v161=v66[v77[2 + 1 ]];v162=nil;v160=1;end end else do return v75[v77[2]];end end elseif ((v78<=(895 -(254 + 595))) or (2610<1230)) then if ((v77[128 -(55 + 71) ]==v75[v77[5 -1 ]]) or (1448==3083)) then v69=v69 + 1 ;else v69=v77[3];end elseif (v78==(1837 -((1856 -(1040 + 243)) + 1217))) then local v239=0 -0 ;local v240;local v241;local v242;local v243;while true do if ((0 -0)==v239) then v240=v77[1 + 1 ];v241,v242=v68(v75[v240](v75[v240 + (1848 -(559 + 1288)) ]));v239=1 -0 ;end if (v239==1) then v70=(v242 + v240) -(940 -(714 + 225)) ;v243=0 -0 ;v239=2 -0 ;end if (v239==2) then for v361=v240,v70 do local v362=0 + (1931 -(609 + 1322)) ;while true do if (0==v362) then v243=v243 + (455 -(13 + 441)) ;v75[v361]=v241[v243];break;end end end break;end end elseif (v77[2 -0 ]==v75[v77[810 -(118 + 688) ]]) then v69=v69 + (49 -(25 + 23)) ;else v69=v77[3];end elseif (v78<=(10 + 41)) then if ((v78<=(1935 -(927 + 959))) or (2827<378)) then v75[v77[6 -(14 -10) ]]=v75[v77[735 -(16 + 716) ]] -v75[v77[7 -3 ]] ;elseif (v78>((384 -237) -((54 -43) + 86))) then if ((3139>916) and ((v75[v77[4 -2 ]]==v77[(11 + 278) -(175 + (399 -289)) ]) or (3476<2597))) then v69=v69 + (2 -1) ;else v69=v77[14 -11 ];end else local v244=1796 -(503 + 1293) ;local v245;while true do if ((2954==2954) and (v244==(0 -0))) then v245=v77[2 + 0 ];v75[v245]=v75[v245](v75[v245 + 1 ]);break;end end end elseif ((3079<4794) and (v78<=(1113 -(810 + 251)))) then do return v75[v77[2 + 0 ]];end elseif (v78>53) then local v246=0 + 0 + 0 ;local v247;while true do if (v246==(0 + 0)) then v247=v77[535 -(43 + 490) ];do return v13(v75,v247,v247 + v77[736 -(711 + 22) ] );end break;end end else v60[v77[3]]=v75[v77[2]];end elseif ((117<=2892) and (v78<=(228 -169))) then if (v78<=56) then if ((v78==(914 -(240 + 619))) or (453>4662)) then v75[v77[1 + 1 ]]();elseif ((1320>595) and (v75[v77[2 -0 ]]~=v75[v77[1 + 3 ]])) then v69=v69 + (1745 -(1344 + 400)) ;else v69=v77[408 -(255 + 150) ];end elseif (v78<=(45 + 12)) then local v165=v77[2 + 0 ];local v166,v167=v68(v75[v165](v13(v75,v165 + 1 ,v77[3])));v70=(v167 + v165) -(4 -3) ;local v168=0;for v190=v165,v70 do v168=v168 + 1 ;v75[v190]=v166[v168];end elseif (v78==(187 -(57 + 72))) then v75[v77[1741 -(404 + 1335) ]]=v75[v77[409 -(183 + 223) ]] + v77[4] ;else v75[v77[2]]=v77[3 -0 ];end elseif ((v78<=(42 + 20)) or (3199<590)) then if ((v78<=(22 + (112 -74))) or (4793<30)) then local v169=v77[339 -(10 + 327) ];v75[v169]=v75[v169](v13(v75,v169 + 1 + 0 + 0 ,v70));elseif (v78>(399 -(118 + 220))) then local v254=v77[1 + 1 ];local v255,v256=v68(v75[v254](v75[v254 + (450 -(108 + 341)) ]));v70=(v256 + v254) -1 ;local v257=0;for v299=v254,v70 do v257=v257 + 1 + (0 -0) ;v75[v299]=v255[v257];end else local v258=v77[(6 + 2) -(4 + 2) ];do return v13(v75,v258,v70);end end elseif (v78<=(1556 -(711 + 782))) then v75[v77[(3 + 0) -1 ]][v77[472 -(270 + 199) ]]=v77[4];elseif ((v78>(21 + 43)) or (1696<=1059)) then if  not v75[v77[(1530 + 291) -(580 + 1239) ]] then v69=v69 + (2 -1) ;else v69=v77[3 + 0 ];end elseif ((2343==2343) and (4854>4464) and v75[v77[1 + 1 ]]) then v69=v69 + 1 ;else v69=v77[3];end elseif (v78<=76) then if (v78<=(31 + 39 + 0)) then if ((v78<=(174 -107)) or (4912==3758)) then if (((126<=3482) and (v78==(42 + 24))) or (1043>3591)) then local v173=v77[1169 -(645 + 522) ];v75[v173]=v75[v173](v13(v75,v173 + (1791 -(1010 + 780)) ,v77[3 + 0 ]));else v75[v77[9 -7 ]]=v75[v77[8 -(438 -(153 + 280)) ]]%v75[v77[1840 -(1045 + 791) ]] ;end elseif (v78<=(171 -103)) then v75[v77[2 -0 ]][v77[508 -(351 + 154) ]]=v75[v77[4]];elseif ((v78==69) or (2890>=4079)) then v75[v77[1576 -((3698 -2417) + 293) ]]=v77[269 -(28 + 238) ] + v75[v77[(8 + 0) -4 ]] ;else v75[v77[1561 -(1381 + 178) ]][v77[3 + 0 ]]=v75[v77[2 + 2 ]];end elseif (v78<=(59 + 14)) then if ((4474<=4770) and (v78<=(31 + 21 + 19))) then local v178=v77[2];v75[v178](v13(v75,v178 + (3 -2) ,v77[2 + 1 ]));elseif (v78>(542 -(381 + 89))) then local v262=0;local v263;local v264;local v265;while true do if ((v262==(1 + 0 + 0)) or (4942==3903)) then v265={};v264=v10({},{__index=function(v363,v364) local v365=0 + 0 ;local v366;while true do if (v365==(0 -0)) then v366=v265[v364];return v366[1157 -(1074 + 82) ][v366[3 -1 ]];end end end,__newindex=function(v367,v368,v369) local v370=v265[v368];v370[1785 -(214 + 1570) ][v370[1457 -(990 + 465) ]]=v369;end});v262=2;end if ((v262==(1 + 0 + 1)) or (248>4845)) then for v372=(668 -(89 + 578)) + 0 ,v77[4 + 0 ] do local v373=0 -0 ;local v374;while true do if ((v373==(1727 -(1668 + 42 + 16))) or (2374==4374)) then if (v374[627 -(512 + (236 -122)) ]==34) then v265[v372-1 ]={v75,v374[5 -2 ]};else v265[v372-(3 -2) ]={v60,v374[3 + 0 ]};end v74[ #v74 + (3 -2) ]=v265;break;end if ((1575==1575) and (v373==0)) then v69=v69 + (1995 -(109 + 1885)) ;v374=v65[v69];v373=1470 -(1269 + 200) ;end end end v75[v77[3 -1 ]]=v29(v263,v264,v61);break;end if ((1569==1569) and (v262==(815 -(14 + 84 + 431 + 286)))) then v263=v66[v77[829 -(96 + 706 + (110 -(84 + 2))) ]];v264=nil;v262=1;end end else v75[v77[2 -0 ]]=v75[v77[3 -0 ]]%v77[1 + 3 ] ;end elseif (v78<=((93 -36) + 17)) then v75[v77[1 + 1 ]]= #v75[v77[1 + 2 ]];elseif (v78>(208 -133)) then local v267=v77[6 -4 ];v75[v267](v75[v267 + 1 ]);else local v268=v77[1 + 1 ];v75[v268]=v75[v268](v13(v75,v268 + 1 ,v77[2 + 1 ]));end elseif (v78<=(68 + 14)) then if ((v78<=(58 + 16 + 5)) or (4927<=3221)) then if (v78<=(919 -(497 + 345))) then if ( not v75[v77[1 + 1 ]] or (2234==1455) or (1780>2787)) then v69=v69 + (1434 -(797 + 17 + 619)) ;else v69=v77[14 -11 ];end elseif ((v78>(1697 -(1427 + 192))) or (3937<=1230)) then local v271=v77[2];do return v13(v75,v271,v70);end else v75[v77[1 + 0 + 1 ]]= #v75[v77[3]];end elseif ((v78<=80) or (2637<1706)) then v69=v77[6 -3 ];elseif ((v78==(73 + 8)) or (2669<=2409)) then v75[v77[1 + 1 ]]=v75[v77[329 -(192 + 134) ]]%v77[1280 -(316 + 960) ] ;else v75[v77[(1335 -(605 + 728)) + 0 ]]={};end elseif (v78<=(66 + 19)) then if (v78<=(77 + 6)) then v60[v77[11 -8 ]]=v75[v77[553 -(83 + 468) ]];elseif (v78==(1890 -(1202 + 604))) then v75[v77[9 -7 ]]=v75[v77[4 -1 ]]%v75[v77[10 -6 ]] ;else local v276=v77[2];local v277=v75[v77[328 -(45 + 280) ]];v75[v276 + 1 + 0 + 0 ]=v277;v75[v276]=v277[v77[4 + 0 ]];end elseif ((v78<=(32 + 54)) or (1067>1779)) then local v183=v77[2 + 0 ];v75[v183]=v75[v183](v75[v183 + (1 -0) + 0 ]);elseif ((2161>=934) and (v78==(160 -73))) then v75[v77[1913 -(340 + 1571) ]]=v60[v77[3]];else v75[v77[1 + 1 ]]=v75[v77[3]] + v75[v77[1776 -(1733 + 39) ]] ;end v69=v69 + 1 ;end end;end return v29(v28(),{},v17)(...);end return v15("LOL!233Q0003063Q00737472696E6703043Q006368617203043Q00627974652Q033Q0073756203053Q0062697433322Q033Q0062697403043Q0062786F7203053Q007461626C6503063Q00636F6E63617403063Q00696E73657274025Q0040544003093Q00E4C8EF45D1D6C949DD03043Q003CB4A48E025Q00405340030C3Q006227583F295BDA433C4B372B03073Q009836483F58453E026Q00534003093Q0037E2A4D702FC82DB0E03043Q00AE678EC5025Q0040514003093Q00FB2D3285B117DBDD2703073Q009CA84E40E0D479025Q00804F4003103Q00F24775069010D7416427BC0CD15D731103063Q007EA7341074D9026Q00364003083Q00323F9A241518BC3903043Q004B6776D9026Q002040030B3Q00A2FD335AFD859EE42652F603063Q00C7EB90523D98027Q004003133Q00DF23D90CBB32BAC024DB0DBA1EB7E72BCC1DBC03073Q00D6894AAB78CE53030C3Q0043726561746542752Q746F6E00454Q00527Q001210000100013Q002009000100010002001210000200013Q002009000200020003001210000300013Q002009000300030004001210000400053Q0006410004000B000100010004503Q000B0001001210000400063Q002009000500040007001210000600083Q002009000600060009001210000700083Q00200900070007000A00062C00083Q000100062Q00223Q00074Q00223Q00014Q00223Q00054Q00223Q00024Q00223Q00034Q00223Q00064Q0002000900083Q001211000A000C3Q001211000B000D4Q004B0009000B00020010443Q000B00092Q0002000900083Q001211000A000F3Q001211000B00104Q004B0009000B00020010443Q000E00092Q0002000900083Q001211000A00123Q001211000B00134Q004B0009000B00020010443Q001100092Q0002000900083Q001211000A00153Q001211000B00164Q004B0009000B00020010443Q001400092Q0002000900083Q001211000A00183Q001211000B00194Q004B0009000B00020010443Q001700092Q0002000900083Q001211000A001B3Q001211000B001C4Q004B0009000B00020010443Q001A00092Q0002000900083Q001211000A001E3Q001211000B001F4Q004B0009000B00020010443Q001D00092Q0002000900083Q001211000A00213Q001211000B00224Q004B0009000B00020010443Q002000092Q005200095Q00062C000A0001000100012Q00227Q00104400090023000A2Q002D000900024Q00233Q00013Q00023Q00023Q00026Q00F03F026Q00704002264Q005200025Q001211000300014Q004A00045Q001211000500013Q00041C0003002100012Q001A00076Q0002000800024Q001A000900014Q001A000A00024Q001A000B00034Q001A000C00044Q0002000D6Q0002000E00063Q00203A000F000600012Q0039000C000F4Q003C000B3Q00022Q001A000C00034Q001A000D00044Q0002000E00014Q004A000F00014Q0054000F0006000F001004000F0001000F2Q004A001000014Q005400100006001000100400100001001000203A0010001000012Q0039000D00104Q0018000C6Q003C000A3Q0002002051000A000A00022Q002F0009000A4Q001600073Q000100040B0003000500012Q001A000300054Q0002000400024Q002B000300044Q003D00036Q00233Q00017Q00293Q00028Q0003043Q0067616D65030A3Q0047657453657276696365027Q0040026Q00F03F026Q000840030E3Q0046696E6446697273744368696C6403083Q00496E7374616E63652Q033Q006E6577026Q00204003043Q004E616D6503043Q0053697A6503053Q005544696D32025Q0080514003083Q00506F736974696F6E025Q00406040026Q005440030B3Q00416E63686F72506F696E7403073Q00566563746F723203053Q00496D61676503103Q004261636B67726F756E64436F6C6F723303063Q00436F6C6F723303073Q0066726F6D524742025Q00E06F4003163Q004261636B67726F756E645472616E73706172656E637903063Q00506172656E74026Q003640030C3Q00436F726E657252616469757303043Q005544696D026Q00244003083Q00546F75636854617003073Q00436F2Q6E656374025Q00405140030C3Q0052657365744F6E537061776E010003073Q00506C6179657273030B3Q004C6F63616C506C61796572030C3Q0057616974466F724368696C64026Q005340025Q00405340025Q0040544002AF3Q001211000200014Q000F000300093Q001211000A00013Q002633000A0062000100010004503Q0062000100263300020011000100010004503Q00110001001210000B00023Q002055000B000B00032Q001A000D5Q002009000D000D00042Q004B000B000D00022Q00020003000B4Q000F000400043Q00062C00043Q000100012Q00223Q00033Q001211000200053Q00263300020061000100060004503Q00610001001211000B00013Q002633000B005D000100010004503Q005D0001002055000C000800072Q0002000E00074Q004B000C000E00022Q00020009000C3Q0006410009005C000100010004503Q005C0001001210000C00083Q002009000C000C00092Q001A000D5Q002009000D000D000A2Q0056000C00020002001044000C000B0007001210000D000D3Q002009000D000D0009001211000E00013Q001211000F000E3Q001211001000013Q0012110011000E4Q004B000D00110002001044000C000C000D001210000D000D3Q002009000D000D0009001211000E00013Q001211000F00103Q001211001000013Q001211001100114Q004B000D00110002001044000C000F000D001210000D00133Q002009000D000D0009001211000E00013Q001211000F00014Q004B000D000F0002001044000C0012000D001044000C00140001001210000D00163Q002009000D000D0017001211000E00183Q001211000F00183Q001211001000184Q004B000D00100002001044000C0015000D00303F000C00190005001044000C001A0008001210000D00083Q002009000D000D00092Q001A000E5Q002009000E000E001B2Q0056000D00020002001210000E001D3Q002009000E000E0009001211000F00013Q0012110010001E4Q004B000E00100002001044000D001C000E001044000D001A000C2Q000A000E5Q00062C000F0001000100022Q00223Q000E4Q00578Q00020010000F4Q00020011000C4Q00060010000200010020090010000C001F00205500100010002000062C00120002000100022Q00223Q000E4Q00223Q00044Q00200010001200014Q000C5Q001211000B00053Q002633000B0014000100050004503Q001400012Q002D000800023Q0004503Q00140001001211000A00053Q002633000A0003000100050004503Q000300010026330002009C000100040004503Q009C0001001211000B00013Q002633000B008B000100050004503Q008B000100064100080089000100010004503Q00890001001211000C00014Q000F000D000D3Q000E2E0001006D0001000C0004503Q006D0001001211000D00013Q002633000D007A000100010004503Q007A0001001210000E00083Q002009000E000E00092Q001A000F5Q002009000F000F00212Q0056000E000200022Q00020008000E3Q0010440008000B0006001211000D00053Q002633000D0070000100050004503Q0070000100303F000800220023001210000E00023Q002009000E000E0024002009000E000E0025002055000E000E00262Q001A00105Q0020090010001000272Q004B000E001000020010440008001A000E0004503Q008900010004503Q007000010004503Q008900010004503Q006D0001001211000200063Q0004503Q009C0001002633000B0067000100010004503Q006700012Q001A000C5Q0020090007000C0028001210000C00023Q002009000C000C0024002009000C000C0025002055000C000C00262Q001A000E5Q002009000E000E00292Q004B000C000E0002002055000C000C00072Q0002000E00064Q004B000C000E00022Q00020008000C3Q001211000B00053Q0004503Q0067000100263300020002000100050004503Q00020001001211000B00013Q000E2E000100A50001000B0004503Q00A500012Q000F000500053Q00062C00050003000100012Q00223Q00033Q001211000B00053Q000E2E0005009F0001000B0004503Q009F00012Q000200065Q001211000200043Q0004503Q000200010004503Q009F00010004503Q000200010004503Q000300010004503Q000200012Q00233Q00013Q00043Q00043Q00030C3Q0053656E644B65794576656E7403043Q00456E756D03073Q004B6579436F6465030B3Q004C656674436F6E74726F6C000A4Q001A7Q0020555Q00012Q000A000200013Q001210000300023Q0020090003000300030020090003000300042Q000A00046Q000F000500054Q00203Q000500012Q00233Q00017Q000A3Q00028Q00026Q00F03F027Q0040030A3Q00496E707574426567616E03073Q00436F2Q6E656374026Q000840030C3Q00496E7075744368616E67656403043Q0067616D65030A3Q0047657453657276696365025Q00804F40012F3Q001211000100014Q000F000200053Q00263300010006000100010004503Q000600012Q000F000200033Q001211000100023Q00263300010015000100030004503Q0015000100062C00053Q000100032Q00223Q00034Q00228Q00223Q00043Q00200900063Q000400205500060006000500062C00080001000100042Q00223Q00044Q00228Q00578Q00223Q00034Q0020000600080001001211000100063Q00263300010019000100020004503Q001900012Q000F000400053Q001211000100033Q00263300010002000100060004503Q0002000100200900063Q000700205500060006000500062C00080002000100012Q00223Q00024Q0020000600080001001210000600083Q0020550006000600092Q001A000800013Q00200900080008000A2Q004B00060008000200200900060006000700205500060006000500062C00080003000100032Q00578Q00223Q00024Q00223Q00054Q00200006000800010004503Q002E00010004503Q000200012Q00233Q00013Q00043Q00073Q0003083Q00506F736974696F6E03053Q005544696D322Q033Q006E657703013Q005803053Q005363616C6503063Q004F2Q6673657403013Q005901193Q00200900013Q00012Q001A00026Q00310001000100022Q001A000200013Q001210000300023Q0020090003000300032Q001A000400023Q0020090004000400040020090004000400052Q001A000500023Q0020090005000500040020090005000500060020090006000100042Q00010005000500062Q001A000600023Q0020090006000600070020090006000600052Q001A000700023Q0020090007000700070020090007000700060020090008000100072Q00010007000700082Q004B0003000700020010440002000100032Q00233Q00017Q00093Q00030D3Q0055736572496E7075745479706503043Q00456E756D030C3Q004D6F75736542752Q746F6E3103053Q00546F756368028Q00026Q00F03F03083Q00506F736974696F6E03073Q004368616E67656403073Q00436F2Q6E656374012A3Q00200900013Q0001001210000200023Q0020090002000200010020090002000200030006290001000C000100020004503Q000C000100200900013Q0001001210000200023Q00200900020002000100200900020002000400061400010029000100020004503Q00290001001211000100053Q00263300010019000100060004503Q001900012Q001A000200013Q0020090002000200072Q005300025Q00200900023Q000800205500020002000900062C00043Q000100022Q00228Q00573Q00024Q00200002000400010004503Q002900010026330001000D000100050004503Q000D0001001211000200053Q00263300020023000100050004503Q002300012Q000A000300014Q0053000300023Q00200900033Q00072Q0053000300033Q001211000200063Q0026330002001C000100060004503Q001C0001001211000100063Q0004503Q000D00010004503Q001C00010004503Q000D00012Q00233Q00013Q00013Q00033Q00030E3Q0055736572496E707574537461746503043Q00456E756D2Q033Q00456E64000A4Q001A7Q0020095Q0001001210000100023Q0020090001000100010020090001000100030006143Q0009000100010004503Q000900012Q000A8Q00533Q00014Q00233Q00017Q00043Q00030D3Q0055736572496E7075745479706503043Q00456E756D030D3Q004D6F7573654D6F76656D656E7403053Q00546F756368010E3Q00200900013Q0001001210000200023Q0020090002000200010020090002000200030006290001000C000100020004503Q000C000100200900013Q0001001210000200023Q0020090002000200010020090002000200040006140001000D000100020004503Q000D00012Q00538Q00233Q00019Q002Q00010A4Q001A00015Q0006400001000900013Q0004503Q000900012Q001A000100013Q0006143Q0009000100010004503Q000900012Q001A000100024Q000200026Q00060001000200012Q00233Q00019Q003Q00064Q001A7Q0006413Q0005000100010004503Q000500012Q001A3Q00014Q002A3Q000100012Q00233Q00017Q00043Q00030C3Q0053656E644B65794576656E7403043Q00456E756D03073Q004B6579436F6465030B3Q004C656674436F6E74726F6C000A4Q001A7Q0020555Q00012Q000A00025Q001210000300023Q0020090003000300030020090003000300042Q000A00046Q000F000500054Q00203Q000500012Q00233Q00017Q00",v9(),...);
