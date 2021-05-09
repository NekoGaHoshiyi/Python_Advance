
from lxml import etree

import random

import requests
import json
import os

user_agents = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
    'Opera/8.0 (Windows NT 5.1; U; en)',
    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0) ',
]
node = {
    # 台海
    'taiwan' :'%22/e3pmh1fmg/e3pmh1g6o%22,%22/e3pmh1fmg/e3pmt8gfv%22,%22/e3pmh1fmg/e3pmt8i3n%22,%22/e3pmh1fmg/e3pmt8lic%22,%22/e3pmh1fmg/e3pmunk13%22,%22/e3pmh1fmg/e3pn6elbj%22',
    # 军事
    'mil' :'%22/e3pmh1dm8/e3pmt7hva%22,%22/e3pmh1dm8/e3pmtdr2r%22,%22/e3pmh1dm8/e3pn62l96%22,%22/e3pmh1dm8/e3pn6f3oh%22',
    # 国际
    'world' :'%22/e3pmh22ph/e3pmh2398%22,%22/e3pmh22ph/e3pmh26vv%22,%22/e3pmh22ph/e3pn6efsl%22,%22/e3pmh22ph/efp8fqe21%22',
    # 国内
    'china' :'%22/e3pmh1nnq/e3pmh1obd%22,%22/e3pmh1nnq/e3pn61c2g%22,%22/e3pmh1nnq/e3pn6eiep%22,%22/e3pmh1nnq/e3pra70uk%22,%22/e3pmh1nnq/e5anm31jb%22,%22/e3pmh1nnq/e7tl4e309%22',
    # 社会
    'society' :'%22/e3pmh19vt/e3pmh1ar3%22,%22/e3pmh19vt/e3pn7fivc%22,%22/e3pmh19vt/e3prv5gfn%22,%22/e3pmh19vt/e3ps21dgq%22,%22/e3pmh19vt/e3ps2ueac%22,%22/e3pmh19vt/e3ps46nfp%22',
    # 体育
    'sports' :'%22/e3pmh3jvm/e3pn4vk37%22,%22/e3pmh3jvm/e3pn4vk37/e3pn61aah%22,%22/e3pmh3jvm/e3pn4vk37/e3pn62b3q%22,%22/e3pmh3jvm/e3pn4vk37/e3pn638jv%22,%22/e3pmh3jvm/e3pn4vk37/e3pn669vr%22,%22/e3pmh3jvm/e3pn4vk37/e82e6tcpo%22,%22/e3pmh3jvm/e3pn61psg%22,%22/e3pmh3jvm/e3pn61psg/e3pn61qfv%22,%22/e3pmh3jvm/e3pn61psg/e7tn9k8oi%22,%22/e3pmh3jvm/e3pn61psg/e7tn9o6uo%22,%22/e3pmh3jvm/e3pn61psg/e7tn9rf8b%22,%22/e3pmh3jvm/e3pn61psg/e7tna015g%22,%22/e3pmh3jvm/e3pn62e6c%22,%22/e3pmh3jvm/e3pn62e6c/e3pn62euk%22,%22/e3pmh3jvm/e3pn62e6c/e3prbvcgu%22,%22/e3pmh3jvm/e3pn62e6c/e82e138l9%22,%22/e3pmh3jvm/e3pn7fhub%22,%22/e3pmh3jvm/e3pn7fhub/e3pn7fif4%22,%22/e3pmh3jvm/e80lb2feu%22',
    # 质量
    'quality' :'%22/e3pmh1m0l/e3pn61c7h%22,%22/e3pmh1m0l/e3pn61hm0%22,%22/e3pmh1m0l/e3pn61ks9%22,%22/e3pmh1m0l/e5at2i193%22,%22/e3pmh1m0l/e5hv56a1p%22,%22/e3pmh1m0l/e7sj13p2a%22,%22/e3pmh1m0l/e7sj17b0r%22,%22/e3pmh1m0l/e7sj1gcbe%22,%22/e3pmh1m0l/e7sj2rsu7%22,%22/e3pmh1m0l/e7sj34723%22,%22/e3pmh1m0l/e7sj3bpu2%22',
    # 房产
    'house' :'%22/e8nf57tcn/e8nf6ch75%22',
    # 教育/留学
    'lx' :'%22/e3pmh20mi/e3pn60gah%22,%22/e3pmh20mi/e3pt1kh3i%22,%22/e3pmh20mi/e7ru9r4mj%22,%22/e3pmh20mi/ectnin83p%22,%22/e3pmh20mi/ectnissc9%22,%22/e3pmh20mi/ectnj650m%22,%22/e3pmh20mi/ectnjgbot%22',
    # 公益
    'hope' :'%22/e3pmh4858/e3pn4u4ek%22,%22/e3pmh4858/e3pttusns%22,%22/e3pmh4858/e3ptucljl%22,%22/e3pmh4858/e3ptucsjk%22,%22/e3pmh4858/e3ptucsjk/e3ptuct5t%22,%22/e3pmh4858/e3ptucsjk/e3ptud330%22,%22/e3pmh4858/e3ptucsjk/e3ptv43ri%22,%22/e3pmh4858/e3ptucsjk/e3ptv5fhm%22,%22/e3pmh4858/e3ptucsjk/e3ptv6vdg%22,%22/e3pmh4858/e3ptucsjk/e3ptva0gc%22,%22/e3pmh4858/e3ptucsjk/e3ptvhqaa%22,%22/e3pmh4858/e3ptucsjk/e3pu014qv%22,%22/e3pmh4858/e3ptucsjk/e3pu0s7q3%22,%22/e3pmh4858/e3ptucsjk/e3pu1b85j%22,%22/e3pmh4858/e3ptucsjk/e3pu20n8h%22,%22/e3pmh4858/e7ksn07g8%22,%22/e3pmh4858/e7ksnbha2%22,%22/e3pmh4858/e7lb8bavn%22,%22/e3pmh4858/e7lb8pe57%22,%22/e3pmh4858/e7lb91aqm%22,%22/e3pmh4858/e7lb99q8k%22,%22/e3pmh4858/e7lhc78q0%22,%22/e3pmh4858/e7lhequu0%22',
    # 时尚
    'fashion' :'%22/e3pn4vu2g/e3pn4vuih%22,%22/e3pn4vu2g/e3pn61569%22,%22/e3pn4vu2g/e3pn7fph9%22,%22/e3pn4vu2g/e3pn7v7f6%22,%22/e3pn4vu2g/e3poftkqs%22,%22/e3pn4vu2g/e3pokk591%22,%22/e3pn4vu2g/e3pokk591/e3pokk5ti%22,%22/e3pn4vu2g/e3pokk591/e3q91thfo%22,%22/e3pn4vu2g/e3pright6%22,%22/e3pn4vu2g/e3prijklc%22,%22/e3pn4vu2g/e3ptq4t9b%22',
    # 娱乐
    'ent' :'%22/e3pmh1jtb/e3pmtdgsc%22,%22/e3pmh1jtb/e3pmtdgsc/e3pmtdhgk%22,%22/e3pmh1jtb/e3pmtdgsc/e3pmtdnnp%22,%22/e3pmh1jtb/e3pmtdgsc/e3pmtdt2b%22,%22/e3pmh1jtb/e3pmtdgsc/e3pn7e7e0%22,%22/e3pmh1jtb/e3pmtdl8t%22,%22/e3pmh1jtb/e3pmtdl8t/e3pmtdlph%22,%22/e3pmh1jtb/e3pmtdl8t/e3pmtgk5g%22,%22/e3pmh1jtb/e3pmtdl8t/e3pmti0d9%22,%22/e3pmh1jtb/e3pmth0vk%22,%22/e3pmh1jtb/e3pmth0vk/e3pmth1kc%22,%22/e3pmh1jtb/e3pmth0vk/e3pmth41r%22,%22/e3pmh1jtb/e3pmth0vk/e3pn61i89%22',
    # 商业
    'biz' :'%22/e3pmh1rv3/e3pmh1sfd%22,%22/e3pmh1rv3/e3pmh2e3h%22,%22/e3pmh1rv3/e3pn60lt0%22,%22/e3pmh1rv3/e3pn60rqk%22,%22/e3pmh1rv3/e3pn60urv%22,%22/e3pmh1rv3/e3pn614r6%22,%22/e3pmh1rv3/e3pn61ned%22,%22/e3pmh1rv3/e3pn62hv9%22,%22/e3pmh1rv3/e3pn63btp%22,%22/e3pmh1rv3/e3pn63m00%22,%22/e3pmh1rv3/e3pok2bl1%22,%22/e3pmh1rv3/e3pu1lrsc%22,%22/e3pmh1rv3/e3pu1okro%22,%22/e3pmh1rv3/e6a3d64vd%22,%22/e3pmh1rv3/e6a3d6rr6%22,%22/e3pmh1rv3/e7nopb37v%22,%22/e3pmh1rv3/e7qcj6l0g%22',
    # 智能
    'smart' :'%22/e3pmh140m/e3pmh14i1%22,%22/e3pmh140m/e3pmh2jgm%22,%22/e3pmh140m/e3pmh31se%22,%22/e3pmh140m/e3pmh4huv%22,%22/e3pmh140m/e3pmh4huv/e3pmh4ign%22,%22/e3pmh140m/e3pn62ehj%22,%22/e3pmh140m/e3pn7fsu3%22,%22/e3pmh140m/e5arbmudl%22,%22/e3pmh140m/e7qeadr4p%22,%22/e3pmh140m/e7qeal82i%22,%22/e3pmh140m/e7qeaudr2%22,%22/e3pmh140m/e7qeb3iev%22,%22/e3pmh140m/e7qeb8nre%22,%22/e3pmh140m/e7qebdhuc%22',
    # 大数据
    'bigdata' :'%22/e3pn606hg/e3pn6072l%22,%22/e3pn606hg/e3pn61287%22,%22/e3pn606hg/e3ptussvj%22,%22/e3pn606hg/e3ptv0m10%22,%22/e3pn606hg/e81jhpqpq%22,%22/e3pn606hg/e81ji3si2%22,%22/e3pn606hg/e81jido1v%22',
    # 评论
    'opinion' :'%22/e3pmub6h5/e3pmub75a%22,%22/e3pmub6h5/e3pn00if8%22,%22/e3pmub6h5/e3pn03vit%22,%22/e3pmub6h5/e3pn4bi4t%22,%22/e3pmub6h5/e3pr9baf6%22,%22/e3pmub6h5/e3prafm0g%22,%22/e3pmub6h5/e3prcgifj%22,%22/e3pmub6h5/e81curi71%22,%22/e3pmub6h5/e81cv14rf%22,%22/e3pmub6h5/e81cv14rf/e81cv52ha%22,%22/e3pmub6h5/e81cv14rf/e81cv7hp0%22,%22/e3pmub6h5/e81cv14rf/e81cvaa3q%22,%22/e3pmub6h5/e81cv14rf/e81cvcd7e%22',
    # 财经
    'finance' :'%22/e3pmh1hmp/e3pmh1iab%22,%22/e3pmh1hmp/e3pn46htn%22,%22/e3pmh1hmp/e3pn60gdi%22,%22/e3pmh1hmp/e3pn60gdi/e3pn60h31%22,%22/e3pmh1hmp/e3pn60gdi/e3pru2fi2%22,%22/e3pmh1hmp/e3pn60rs2%22,%22/e3pmh1hmp/e3pn60rs2/e3pn60skq%22,%22/e3pmh1hmp/e3pn60rs2/e3ptlr015%22,%22/e3pmh1hmp/e3pn61831%22,%22/e3pmh1hmp/e3pn61an9%22,%22/e3pmh1hmp/e3pn61chp%22,%22/e3pmh1hmp/e3pn62ihu%22,%22/e3pmh1hmp/e3pn62uuq%22,%22/e3pmh1hmp/e3pn6314j%22,%22/e3pmh1hmp/e3pn6314j/e3pn6323a%22,%22/e3pmh1hmp/e3pn6314j/e3ptma9ah%22,%22/e3pmh1hmp/e3ptkencb%22,%22/e3pmh1hmp/e3ptlrdc9%22,%22/e3pmh1hmp/e3ptlrdc9/e3ptltkc2%22,%22/e3pmh1hmp/e3ptlrdc9/e3ptm2ci2%22,%22/e3pmh1hmp/e7i6qafud%22,%22/e3pmh1hmp/e7i6t8c0j%22,%22/e3pmh1hmp/e7lipkhq1%22,%22/e3pmh1hmp/e7lipkhq1/e7lipkii0%22,%22/e3pmh1hmp/e7lipkhq1/e7o08h1r8%22',
    # 科技
    'tech' :'%22/e3pmh164r/e3pmh2hq8%22,%22/e3pmh164r/e3pmh33i9%22,%22/e3pmh164r/e3pmh356p%22,%22/e3pmh164r/e3pmh3dh4%22,%22/e3pmh164r/e3pmtlao3%22,%22/e3pmh164r/e3pmtm015%22,%22/e3pmh164r/e3pmtnh4j%22,%22/e3pmh164r/e3pn1fd3s%22,%22/e3pmh164r/e3pn46ri0%22,%22/e3pmh164r/e3pn4bn46%22,%22/e3pmh164r/e3pn4gh77%22,%22/e3pmh164r/e3pn4qlss%22,%22/e3pmh164r/e3pn6fo08%22,%22/e3pmh164r/e3ptqlvrg%22',
    # 汽车
    'auto' :'%22/e3pmh24qk/e3pmh25cs%22,%22/e3pmh24qk/e3pmtj57c%22,%22/e3pmh24qk/e3pmtkgc2%22,%22/e3pmh24qk/e3pn02mp3%22,%22/e3pmh24qk/e3pn4el6u%22,%22/e3pmh24qk/ej8aajlga%22',
    # 艺术
    'art' :'%22/e3pokdnam/e3pokdnrj%22',
    # 旅游
    'go' :'/e3pmh1tuv/e3pmh1ufv/e3pmh1v35&tags=%22%E5%87%BA%E6%B8%B8%22',
    # 健康
    'health' :'%22/e3pmt7dq2/e3pmt7edc%22,%22/e3pmt7dq2/e3pmt904n%22,%22/e3pmt7dq2/e3pmt9htm%22,%22/e3pmt7dq2/e3pmtbedk%22,%22/e3pmt7dq2/e3pmtvmsa%22,%22/e3pmt7dq2/e3pn49kc7%22,%22/e3pmt7dq2/e3pn4cagl%22,%22/e3pmt7dq2/e3pn4f81k%22,%22/e3pmt7dq2/e3pn50ich%22,%22/e3pmt7dq2/e3pn61f01%22,%22/e3pmt7dq2/e3pn6edle%22,%22/e3pmt7dq2/e3pn6gvs7%22,%22/e3pmt7dq2/e3prd5mi2%22,%22/e3pmt7dq2/e3ptds3rp%22,%22/e3pmt7dq2/e3ptds3rp/e3ptds4r8%22,%22/e3pmt7dq2/e3ptt66fi%22',
    # 亲子
    'qinzi' :'%22/ebggoaf45/ebgmgut3n%22,%22/ebggoaf45/ebgmgut3n/ebgmhivbk%22,%22/ebggoaf45/ebgmi0d9i%22,%22/ebggoaf45/ebgmi0d9i/ebi36o0qb%22,%22/ebggoaf45/ebi37sp8n%22,%22/ebggoaf45/ebi37sp8n/ebi388sjn%22,%22/ebggoaf45/ebi38m5d7%22,%22/ebggoaf45/ebi38m5d7/ebi391j8t%22,%22/ebggoaf45/ebi39m4up%22,%22/ebggoaf45/ebi39m4up/ebi39uvki%22',
    # 城市
    'city' :'%22/e3pmh1nv4/e3pn60pg4%22,%22/e3pmh1nv4/e3pn637a1%22,%22/e3pmh1nv4/e3pu0ucu5%22,%22/e3pmh1nv4/e7td1g6u2%22,%22/e3pmh1nv4/e7td1t7it%22,%22/e3pmh1nv4/ecko2h4rc%22,%22/e3pmh1nv4/ecko2on6j%22,%22/e3pmh1nv4/ecko30dgg%22&offset=60',
    # 博览/杂烩
    'look' :'%22/e3pn4q8sp/e3pn4q9gc%22,%22/e3pn4q8sp/e3pn7ibfm%22,%22/e3pn4q8sp/e3pofukpl%22,%22/e3pn4q8sp/e3pttoksk%22',
    # 长三角
    'yrd' :'%22/e3pu6i31u/eecbiskt4%22,%22/e3pu6i31u/eecc32cqf%22,%22/e3pu6i31u/eecc35cit%22,%22/e3pu6i31u/eecc38g1f%22,%22/e3pu6i31u/eecc3c3fq%22,%22/e3pu6i31u/eecc3f0eh%22,%22/e3pu6i31u/eecc3i4cj%22,%22/e3pu6i31u/eecc3lq5n%22,%22/e3pu6i31u/eecc3om9o%22,%22/e3pu6i31u/eecc3rbnu%22',
    # 海外看中国
    'oversea' :'%22/e3pmt7bdh/e3pn4bc7q%22,%22/e3pmt7bdh/e3pn5250c%22,%22/e3pmt7bdh/e3pn6g8t8%22',
    # 文化
    'cul' :'%22/e3pn677q4/e3ptvpbdi%22,%22/e3pn677q4/e7n7nshou%22,%22/e3pn677q4/e7n7nshou/e7n7o5sgv%22,%22/e3pn677q4/e7n7nshou/e7n7oddi8%22,%22/e3pn677q4/e7n7nshou/e7n7oj8js%22,%22/e3pn677q4/e7n7nshou/e7n7opklk%22,%22/e3pn677q4/e7n7nshou/e80schtc2%22,%22/e3pn677q4/e7n7qip93%22,%22/e3pn677q4/e7n7qip93/e7n7quqav%22,%22/e3pn677q4/e7n7qip93/e7n7r604h%22,%22/e3pn677q4/e7n7qip93/e7n7rlouf%22,%22/e3pn677q4/e7n7s45fv%22,%22/e3pn677q4/e7n7s45fv/e7n7safa1%22,%22/e3pn677q4/e7n7s45fv/e7n7silkh%22,%22/e3pn677q4/e7n7s45fv/e7n7sqsjs%22,%22/e3pn677q4/e7n836lt3%22,%22/e3pn677q4/e7n83ff31%22,%22/e3pn677q4/e7n83ff31/e7n83ll7b%22,%22/e3pn677q4/e7n83ff31/e7n83scbg%22,%22/e3pn677q4/e7n83ff31/e7n8421o7%22,%22/e3pn677q4/e7n84b0u1%22,%22/e3pn677q4/e7n84le0h%22,%22/e3pn677q4/e7n856422%22',
    # 创投
    'capital' :'%22/e5d59phvs/e5d5m10mv%22,%22/e5d59phvs/e5d5m10mv/e5d5o560g%22,%22/e5d59phvs/e5d5m10mv/e5d5oecei%22,%22/e5d59phvs/e5d5m10mv/e5d5pk5dq%22,%22/e5d59phvs/e5d5m10mv/e5d5q73kg%22,%22/e5d59phvs/e5d5qjh4s%22,%22/e5d59phvs/e5d5qjh4s/e5d5qp63c%22,%22/e5d59phvs/e5d5qjh4s/e5d5sanu9%22,%22/e5d59phvs/e5d5qjh4s/e5d5sjom2%22,%22/e5d59phvs/e5d5svess%22,%22/e5d59phvs/e5d5svess/e5d5t6l0v%22,%22/e5d59phvs/e5d5svess/e5d5tee08%22,%22/e5d59phvs/e5d5svess/e5d5tp81t%22,%22/e5d59phvs/e5d5svess/e5d5tvudv%22,%22/e5d59phvs/e5d5u9tt0%22,%22/e5d59phvs/e5d5u9tt0/e5d5uf626%22,%22/e5d59phvs/e5d5u9tt0/e5d5uktk9%22,%22/e5d59phvs/e5d5u9tt0/e5d5uqcrs%22,%22/e5d59phvs/e5d5u9tt0/e5d5v01f0%22,%22/e5d59phvs/e63f43ge6%22,%22/e5d59phvs/e63f43ge6/e63f43h0u%22,%22/e5d59phvs/e63f43ge6/e63fcq9bt%22,%22/e5d59phvs/e63j24g2m%22,%22/e5d59phvs/e63j24g2m/e63j24goo%22',
    # 商协
    'chamber' :'%22/e3pu1oj7h/e3pu1ok69%22',
    # 无人机
    'uav' :'%22/e3pn5tffs/e3pn5tg0p%22,%22/e3pn5tffs/e3pn5tg0p/e3ptjsfnn%22,%22/e3pn5tffs/e3pn6156o%22,%22/e3pn5tffs/e3poit9nf%22,%22/e3pn5tffs/e3poit9nf/e3ptjtt1d%22,%22/e3pn5tffs/e3pshm06b%22,%22/e3pn5tffs/e3pthq9rg%22,%22/e3pn5tffs/e3ptkjts8%22,%22/e3pn5tffs/e5ar1t85q%22,%22/e3pn5tffs/e7rugtglo%22,%22/e3pn5tffs/e7ruia4rh%22,%22/e3pn5tffs/e7siujt5c%22',
    #
}

def craw_huanqiu(category, loop):
    # 最大以25为单位
    if not os.path.exists('./huanqiu_news/'):  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs('./huanqiu_news/')
    wf = open('./huanqiu_news/huanqiu_ ' +category +'.txt', 'w', encoding='utf-8')
    base_url = "https:// " +category +".huanqiu.com/api/list?node= "+ \
               node[category ] +"&offset=start&limit=20"
    base_url2 = "https:// "+ category +".huanqiu.com/article/"
    for i in range(0, loop):
        url = base_url.replace('start', str(i * 30)).replace(' ','')
        print(url)
        #https: // mil.huanqiu.com / api / list?node = % 22 / e3pmh1dm8 / e3pmt7hva % 22, % 22 / e3pmh1dm8 / e3pmtdr2r % 22, % 22 / e3pmh1dm8 / e3pn62l96 % 22, % 22 / e3pmh1dm8 / e3pn6f3oh % 22 & offset = 20 & limit = 20
        #https: // mil.huanqiu.com / api / list?node = % 22 / e3pmh1dm8 / e3pmt7hva % 22, % 22 / e3pmh1dm8 / e3pmtdr2r % 22, % 22 / e3pmh1dm8 / e3pn62l96 % 22, % 22 / e3pmh1dm8 / e3pn6f3oh % 22 & offset = 0 & limit = 20
        res = requests.get(url,
                           headers={'User-Agent': random.choice(user_agents)})
        html = res.text
        news_dic = json.loads(html)
        # print(news_dic['list'])
        for item in news_dic['list']:
            if 'source' not in item or item['source']['url'] == None:
                continue
            sub_url = base_url2 + item['aid']
            sub_res = requests.get(sub_url.replace(' ',''),
                                   headers={'User-Agent': random.choice(user_agents)})
            sub_res.encoding = 'utf-8'
            sub_html = sub_res.text
            sub_html = etree.HTML(sub_html)
            # print(item['source']['url'])
            contents = ''.join(sub_html.xpath(".//section//p/text()")).strip()
            title = item['title']
            print(item['title'] + ':' + contents)
            ntime = sub_html.xpath(".// div[ @class ='metadata-info']/p/text()")[0].strip()
            source = sub_html.xpath(".//div[@class='metadata-info']/p/span/span//text()")[0].strip()
            link = sub_url
            if contents == '':
                continue
            else:
                wf.write(ntime + '^' + contents + '^' + title + '^' +
                         source + '^' + link + '\n')
    wf.close()


# 第一个参数门类参考分类页的url，例如台海页面是https://taiwan.huanqiu.com/，则门类是taiwan
# 第二个参数是获取的数据量，数值越大获取越多
# world,mil，tanwan,
#craw_huanqiu('mil', 50)
#craw_huanqiu('world', 50)
#craw_huanqiu('taiwan', 50)
