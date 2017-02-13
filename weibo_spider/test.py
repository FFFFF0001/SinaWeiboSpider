#!/usr/bin/python
# coding: utf-8

"""
    Author: YuJun
    Email: cuteuy@gmail.com
    Date created: 2017/1/19
"""
import re
from scrapy import Selector
doc = """
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"><html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><meta http-equiv="Cache-Control" content="no-cache"/><meta id="viewport" name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0, maximum-scale=2.0" /><link rel="icon" sizes="any" mask href="http://h5.sinaimg.cn/upload/2015/05/15/28/WeiboLogoCh.svg" color="black"><meta name="MobileOptimized" content="240"/><title>评论列表</title><style type="text/css" id="internalStyle">html,body,p,form,div,table,textarea,input,span,select{font-size:12px;word-wrap:break-word;}body{background:#F8F9F9;color:#000;padding:1px;margin:1px;}table,tr,td{border-width:0px;margin:0px;padding:0px;}form{margin:0px;padding:0px;border:0px;}textarea{border:1px solid #96c1e6}textarea{width:95%;}a,.tl{color:#2a5492;text-decoration:underline;}/*a:link {color:#023298}*/.k{color:#2a5492;text-decoration:underline;}.kt{color:#F00;}.ib{border:1px solid #C1C1C1;}.pm,.pmy{clear:both;background:#ffffff;color:#676566;border:1px solid #b1cee7;padding:3px;margin:2px 1px;overflow:hidden;}.pms{clear:both;background:#c8d9f3;color:#666666;padding:3px;margin:0 1px;overflow:hidden;}.pmst{margin-top: 5px;}.pmsl{clear:both;padding:3px;margin:0 1px;overflow:hidden;}.pmy{background:#DADADA;border:1px solid #F8F8F8;}.t{padding:0px;margin:0px;height:35px;}.b{background:#e3efff;text-align:center;color:#2a5492;clear:both;padding:4px;}.bl{color:#2a5492;}.n{clear:both;background:#436193;color:#FFF;padding:4px; margin: 1px;}.nt{color:#b9e7ff;}.nl{color:#FFF;text-decoration:none;}.nfw{clear:both;border:1px solid #BACDEB;padding:3px;margin:2px 1px;}.s{border-bottom:1px dotted #666666;margin:3px;clear:both;}.tip{clear:both; background:#c8d9f3;color:#676566;border:1px solid #BACDEB;padding:3px;margin:2px 1px;}.tip2{color:#000000;padding:2px 3px;clear:both;}.ps{clear:both;background:#FFF;color:#676566;border:1px solid #BACDEB;padding:3px;margin:2px 1px;}.tm{background:#feffe5;border:1px solid #e6de8d;padding:4px;}.tm a{color:#ba8300;}.tmn{color:#f00}.tk{color:#ffffff}.tc{color:#63676A;}.c{padding:2px 5px;}.c div a img{border:1px solid #C1C1C1;}.ct{color:#9d9d9d;font-style:italic;}.cmt{color:#9d9d9d;}.ctt{color:#000;}.cc{color:#2a5492;}.nk{color:#2a5492;}.por {border: 1px solid #CCCCCC;height:50px;width:50px;}.me{color:#000000;background:#FEDFDF;padding:2px 5px;}.pa{padding:2px 4px;}.nm{margin:10px 5px;padding:2px;}.hm{padding:5px;background:#FFF;color:#63676A;}.u{margin:2px 1px;background:#ffffff;border:1px solid #b1cee7;}.ut{padding:2px 3px;}.cd{text-align:center;}.r{color:#F00;}.g{color:#0F0;}.bn{background: transparent;border: 0 none;text-align: left;padding-left: 0;}</style><script>if(top != self){top.location = self.location;}</script></head><body><div class="n" style="padding: 6px 4px;"><a href="http://weibo.cn/?tf=5_009" class="nl">首页</a>|<a href="http://weibo.cn/msg/?tf=5_010" class="nl">消息</a>|<a href="http://huati.weibo.cn" class="nl">话题</a>|<a href="http://weibo.cn/search/?tf=5_012" class="nl">搜索</a>|<a href="/comment/EroNT3sSm?uid=2678002132&amp;rl=0&amp;rand=4049&amp;p=r" class="nl">刷新</a></div><div class="s"></div><div class="c" id="M_"><div>    <a href="/ihciah">窝要萌萌哒</a><img src="http://h5.sinaimg.cn/upload/2016/05/26/319/5338.gif" alt="V"/>    <span class="cmt">&nbsp;转发了&nbsp;<a href="/u/3170766712">@如皋老猫</a><img src="http://h5.sinaimg.cn/upload/2016/05/26/319/5338.gif" alt="V"/><img src="http://h5.sinaimg.cn/upload/2016/05/26/319/donate_btn_s.png" alt="M"/>&nbsp;的微博:</span><span class="ctt">我看了都喘不过气来了 <a href="http://weibo.cn/sinaurl?f=w&amp;u=http%3A%2F%2Ft.cn%2FRMEGVID&amp;ep=EroNT3sSm%2C2678002132%2CErgVLBc1y%2C3170766712">秒拍视频</a> . ​​​</span>                    &nbsp;<span class="cmt">原文转发[30971]</span>    &nbsp;<a href="/comment/ErgVLBc1y#cmtfrm" class="cc">原文评论[18158]</a>    </div>    <div><span class="cmt">转发理由:</span>    转发微博        <!-- 是否进行翻译 -->        &nbsp;    <span class="ct">01月18日 16:10    </span>        &nbsp;<a href="/spam/?mid=EroNT3sSm&amp;fuid=2678002132&amp;type=1&amp;rl=1">举报</a>&nbsp;<a href="/fav/addFav/EroNT3sSm?rl=1&amp;st=0d0319">收藏</a>&nbsp;<a href="/mblog/operation/EroNT3sSm?uid=2678002132&amp;rl=1" >操作</a>    </div></div><div class="c"></div><div><span>&nbsp;<a href="/repost/EroNT3sSm?uid=2678002132&amp;#rt">转发[1]</a>&nbsp;</span><span class="pms">&nbsp;评论[2]&nbsp;</span><span >&nbsp;<a href="/attitude/EroNT3sSm?#attitude">赞[1]</a>&nbsp;</span><br/></div><div class="pms" id="cmtfrm"><form action="/comments/addcomment?st=0d0319" method="post"><div>    评论只显示前140字:<br/>    <input type="hidden" name="srcuid" value="2678002132" />    <input type="hidden" name="id" value="EroNT3sSm" />        <input type="hidden" name="rl" value="1" />    <textarea name="content" rows="2" cols="20"></textarea><br/>        <input type="submit" value="评论" />&nbsp;<input type="submit" value="评论并转发" name="rt" /></div></form></div><div class="c" id="C_4065324653292967">        <a href="/u/3905394736">Mo夏目</a>        :<span class="ctt">他坐的是假车[哈哈]</span>    &nbsp;<a href="/spam/?cid=4065324653292967&amp;fuid=3905394736&amp;type=2&amp;rl=1">举报</a>    &nbsp;    <span class="cc">    <a href="/attitude/ErpoldOEn/update?object_type=comment&amp;uid=3776493371&amp;rl=1&amp;st=0d0319">赞[0]</a></span>        &nbsp;<span class="cc"><a href="/comments/reply/EroNT3sSm/4065324653292967?rl=1&amp;st=0d0319">回复</a></span>        &nbsp;    <span class="ct">01月18日 17:39&nbsp;来自微博 weibo.com    </span></div>    <div class="s"></div>            <div class="c" id="C_4065306919938247">        <a href="/skyduy">Skyduy丶</a>        :<span class="ctt">................</span>    &nbsp;<a href="/spam/?cid=4065306919938247&amp;fuid=3776493371&amp;type=2&amp;rl=1">举报</a>    &nbsp;    <span class="cc">    <a href="/attitude/EroVJFHoj/update?object_type=comment&amp;uid=3776493371&amp;rl=1&amp;st=0d0319">赞[0]</a></span>        &nbsp;<span class="cc"><a href="/comments/reply/EroNT3sSm/4065306919938247?rl=1&amp;st=0d0319">回复</a></span>    &nbsp;<span class="cc"><a href="/comments/del/EroNT3sSm/4065306919938247?rl=1&amp;cmtuid=3776493371">删除</a></span>        &nbsp;    <span class="ct">01月18日 16:29&nbsp;来自微博 weibo.com    </span></div>        <div class="s"></div></body></html>"""


selector = Selector(text=doc)

comments = selector.xpath('body/div[@class="c" and @id]')
for comment in comments:
    comment_id = comment.xpath('@id').extract_first()  # comment_id
    if comment_id == 'M_':
        continue
    auth_id = re.findall(u'fuid=(.*?)&type', comment.xpath('a/@href').extract()[1])[0]  # auth_id
    content = comment.xpath('span[@class="ctt"]')  # 内容，回复对象
    text = content.xpath('text()').extract()

    print auth_id, text[0]
