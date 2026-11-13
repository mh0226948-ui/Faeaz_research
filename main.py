import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="امور پژوهشی فراز", docs_url=None, redoc_url=None)

HTML = """<!doctype html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="امور پژوهشی فراز؛ خدمات مشاوره و پشتیبانی پژوهشی، پایان‌نامه، مقاله و تحلیل آماری">
<title>امور پژوهشی فراز</title>
<style>
:root{--navy:#10243a;--gold:#c9a45c;--paper:#f6f7fa}*{box-sizing:border-box}
body{margin:0;font-family:Tahoma,Arial,sans-serif;background:var(--paper);color:#1d2937;line-height:1.9}
header{background:linear-gradient(120deg,#10243a,#1c3c58);color:white;padding:24px max(6%,calc((100% - 1100px)/2))}
.brand{font-size:26px;font-weight:800;color:#f0cf86}nav{display:flex;gap:20px;flex-wrap:wrap;margin-top:12px}a{color:inherit;text-decoration:none}
.hero{padding:72px 6%;text-align:center;background:white}.hero h1{font-size:clamp(28px,5vw,44px);color:var(--navy);margin:0 0 12px}
.hero p{max-width:760px;margin:0 auto 24px;color:#536273}.btn{display:inline-block;background:var(--gold);color:#142638;padding:10px 24px;border-radius:10px;font-weight:bold}
main{max-width:1100px;margin:38px auto;padding:0 18px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:16px}
.card{background:white;padding:20px;border-radius:14px;box-shadow:0 5px 22px #1426380d}.card h3{color:var(--navy);margin-top:0}
h2{color:var(--navy)}footer{margin-top:50px;background:var(--navy);color:#e8edf2;padding:30px 6%;text-align:center}
</style></head>
<body><header><div class="brand">امور پژوهشی فراز</div><div>همراه مطمئن مسیر پژوهش شما</div><nav><a href="#services">خدمات</a><a href="#about">درباره ما</a><a href="#contact">ارتباط با ما</a></nav></header>
<section class="hero"><h1>از ایده تا ارائه؛ در کنار مسیر پژوهش شما</h1><p>خدمات مشاوره و پشتیبانی پژوهشی، تحلیل آماری، آماده‌سازی ارائه و خدمات دانشجویی با رویکردی دقیق و مسئولانه.</p><a class="btn" href="#contact">درخواست مشاوره</a></section>
<main><section id="services"><h2>خدمات ما</h2><div class="grid">
<div class="card"><h3>پایان‌نامه و پروپوزال</h3><p>مشاوره موضوع، تدوین ساختار و همراهی در مسیر پژوهش.</p></div>
<div class="card"><h3>مقاله و پژوهش</h3><p>راهنمایی در نگارش علمی، ویرایش و آماده‌سازی مقاله.</p></div>
<div class="card"><h3>تحلیل آماری</h3><p>مشاوره انتخاب روش تحلیل و تفسیر نتایج پژوهش.</p></div>
<div class="card"><h3>پاورپوینت و ارائه</h3><p>طراحی ارائه‌های دانشگاهی و اسلایدهای دفاع.</p></div>
<div class="card"><h3>پرسشنامه</h3><p>طراحی و پیاده‌سازی پرسشنامه‌های دیجیتال.</p></div>
<div class="card"><h3>امور دانشجویی</h3><p>راهنمایی و پشتیبانی در امور و فرایندهای دانشجویی.</p></div>
</div></section><section id="about"><h2>درباره فراز</h2><div class="card"><p>فراز با هدف ساده‌تر کردن مسیر انجام فعالیت‌های پژوهشی و دانشگاهی شکل گرفته است. جزئیات خدمات و شرایط همکاری پیش از شروع هر سفارش با مشتری هماهنگ می‌شود.</p></div></section>
<section id="contact"><h2>ارتباط با ما</h2><div class="card"><p>برای دریافت مشاوره و اطلاع از شرایط خدمات، از راه ارتباطی مجموعه استفاده کنید.</p><p>شماره تماس و نشانی شبکه‌های اجتماعی پس از تنظیم اطلاعات مدیر در نسخه نهایی درج می‌شود.</p></div></section></main>
<footer>© امور پژوهشی فراز — کلیه حقوق محفوظ است</footer></body></html>"""

@app.get("/", response_class=HTMLResponse)
def home():
    return HTML

@app.get("/health")
def health():
    return {"status": "ok", "service": "faraz-research"}
