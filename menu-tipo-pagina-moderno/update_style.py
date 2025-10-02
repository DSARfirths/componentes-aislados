import re
from pathlib import Path

ENC = 'iso-8859-1'
PATH = Path(r"c:\Users\HP RYZEN 7\Downloads\menu-tipo-pagina-moderno\index.html")
text = PATH.read_text(encoding=ENC)

style_block = """<style>
  @import url('https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600;700&display=swap');
  :root{
    --brand-black: #000000;
    --brand-white: #ffffff;
    --accent-femme: #ff2193;
    --accent-homme: #1151bb;
    --accent-couple: #0098d5;
    --muted: #5d5b66;
    --surface: #ffffff;
    --surface-soft: #f5f7fb;
    --outline: rgba(0,0,0,.08);
    --sheet-accent: var(--accent-femme);
    --nav-h: 72px;
    --radius: 18px;
    --gutter: clamp(14px, 4vw, 36px);
    --speed: 360ms;
    --shadow-soft: 0 30px 60px rgba(15,17,32,.12);
    --font-ui: "Jost", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    --fs-00: clamp(.8125rem, .78rem + .15vw, .875rem);
    --fs-0: clamp(.875rem, .78rem + .20vw, 1rem);
    --fs-1: clamp(1rem, .92rem + .30vw, 1.125rem);
    --fs-2: clamp(1.125rem, 1rem + .60vw, 1.5rem);
  }

  *,*::before,*::after{box-sizing:border-box;}
  html,body{height:100%;}
  body{
    margin:0;
    font-family:var(--font-ui);
    font-size:var(--fs-0);
    color:var(--brand-black);
    background:linear-gradient(180deg,#ffffff 0%,#f8f9fc 100%);
    line-height:1.5;
    -webkit-font-smoothing:antialiased;
  }
  a{color:inherit;text-decoration:none;}
  button{font:inherit;}

  header{
    position:sticky;
    top:0;
    z-index:50;
    height:var(--nav-h);
    display:flex;
    align-items:center;
    justify-content:center;
    padding:0 var(--gutter);
    background:#000000;
    color:var(--brand-white);
    border-bottom:1px solid rgba(255,255,255,.08);
    box-shadow:0 12px 32px rgba(0,0,0,.35);
  }
  .header-inner{
    width:min(1200px,100%);
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:20px;
  }
  .brand{
    font-weight:700;
    letter-spacing:.16em;
    text-transform:uppercase;
    font-size:clamp(.95rem, .8rem + .7vw, 1.25rem);
    color:var(--brand-white);
    white-space:nowrap;
  }

  nav.primary{
    display:flex;
    gap:10px;
    align-items:center;
    padding:6px 8px;
    border-radius:999px;
    background:rgba(255,255,255,.08);
    backdrop-filter:blur(12px);
  }
  .nav-btn{
    position:relative;
    border:0;
    background:transparent;
    color:var(--brand-white);
    padding:12px 22px;
    border-radius:999px;
    font-weight:600;
    font-size:var(--fs-2);
    letter-spacing:.06em;
    text-transform:uppercase;
    transition:color .3s ease, transform .3s ease;
    isolation:isolate;
    cursor:pointer;
  }
  .nav-btn::before{
    content:'';
    position:absolute;
    inset:0;
    background:linear-gradient(90deg, rgba(255,255,255,.22) 0%, var(--accent, var(--accent-femme)) 100%);
    opacity:0;
    border-radius:inherit;
    transition:opacity .3s ease, transform .3s ease;
    z-index:-1;
  }
  .nav-btn:hover,
  .nav-btn:focus-visible{
    transform:translateY(-2px);
  }
  .nav-btn:hover::before,
  .nav-btn:focus-visible::before{
    opacity:.25;
  }
  .nav-btn:focus-visible{
    outline:2px solid rgba(255,255,255,.6);
    outline-offset:4px;
  }
  .nav-btn[aria-expanded="true"]{
    color:var(--brand-black);
  }
  .nav-btn[aria-expanded="true"]::before{
    opacity:1;
    transform:scale(1.02);
  }

  .hamburger{
    position:fixed;
    top:calc((var(--nav-h) - 48px)/2);
    right:var(--gutter);
    width:48px;
    height:48px;
    border-radius:14px;
    border:1px solid rgba(255,255,255,.25);
    background:rgba(255,255,255,.1);
    color:var(--brand-white);
    display:none;
    place-items:center;
    cursor:pointer;
    z-index:52;
    transition:transform .35s ease, background .35s ease, border-color .35s ease;
  }
  .hamburger:hover{
    transform:translateY(-2px);
    background:rgba(255,255,255,.18);
  }
  .hamburger .bar{
    position:absolute;
    left:50%;
    top:50%;
    width:26px;
    height:2px;
    background:currentColor;
    border-radius:2px;
    transform-origin:center;
    transition:transform .45s cubic-bezier(.2,1,.3,1), opacity .3s ease;
  }
  .hamburger .bar:nth-child(1){transform:translate(-50%,-50%) translateY(-6px);}
  .hamburger .bar:nth-child(2){transform:translate(-50%,-50%);}
  .hamburger .bar:nth-child(3){transform:translate(-50%,-50%) translateY(6px);}
  .hamburger[aria-expanded="true"]{
    background:rgba(0,0,0,.85);
    border-color:rgba(255,255,255,.35);
  }
  .hamburger[aria-expanded="true"] .bar:nth-child(1){transform:translate(-50%,-50%) rotate(45deg);}
  .hamburger[aria-expanded="true"] .bar:nth-child(2){opacity:0; transform:translate(-50%,-50%) scaleX(.5);}
  .hamburger[aria-expanded="true"] .bar:nth-child(3){transform:translate(-50%,-50%) rotate(-45deg);}

  .desk-backdrop{
    position:fixed;
    inset:0;
    background:rgba(0,0,0,.55);
    opacity:0;
    pointer-events:none;
    transition:opacity .35s ease;
    z-index:45;
  }
  .desk-backdrop.open{
    opacity:1;
    pointer-events:auto;
  }

  .desk-sheet{
    position:fixed;
    inset:0;
    background:#050505;
    color:var(--brand-white);
    z-index:46;
    transform:translateY(-100%);
    opacity:0;
    pointer-events:none;
    transition:transform .45s cubic-bezier(.2,1,.3,1), opacity .4s ease;
    display:flex;
    align-items:center;
    justify-content:center;
    padding:var(--gutter);
  }
  .desk-sheet::after{
    content:'';
    position:absolute;
    inset:10%;
    border:1px solid rgba(255,255,255,.05);
    border-radius:36px;
    pointer-events:none;
  }
  .desk-sheet.open{
    transform:translateY(0);
    opacity:1;
    pointer-events:auto;
  }
  .desk-sheet-content{
    width:min(1180px,100%);
    padding:clamp(24px,3vw,48px);
    display:flex;
    flex-direction:column;
    gap:32px;
  }
  .desk-sheet-head{
    font-size:clamp(1.45rem,1.1rem + 1vw,2.2rem);
    font-weight:600;
    text-transform:uppercase;
    letter-spacing:.18em;
    color:var(--sheet-accent);
  }
  .desk-sheet-grid{
    display:grid;
    grid-template-columns:repeat(3,minmax(0,1fr));
    gap:clamp(20px,3vw,40px);
  }
  .desk-col{display:flex;flex-direction:column;gap:28px;}
  .desk-section{
    display:flex;
    flex-direction:column;
    gap:12px;
  }
  .desk-section-title{
    margin:0;
    font-size:var(--fs-1);
    font-weight:600;
    color:var(--sheet-accent);
    letter-spacing:.08em;
    text-transform:uppercase;
  }
  .desk-sublist{
    list-style:none;
    margin:0;
    padding:0;
    display:grid;
    gap:10px;
  }
  .desk-subitem{
    position:relative;
    display:block;
    padding:12px 16px;
    border-radius:14px;
    background:rgba(255,255,255,.08);
    color:var(--brand-white);
    font-weight:500;
    letter-spacing:.04em;
    transition:transform .3s ease, background .3s ease, box-shadow .3s ease, opacity .35s ease;
    opacity:0;
    transform:translateY(12px);
  }
  .desk-subitem::after{
    content:'';
    position:absolute;
    inset:0;
    border-radius:inherit;
    border:1px solid rgba(255,255,255,.08);
    transition:border-color .3s ease;
  }
  .desk-subitem.is-visible{
    opacity:1;
    transform:translateY(0);
  }
  .desk-subitem:hover,
  .desk-subitem:focus-visible{
    background:linear-gradient(90deg, rgba(255,255,255,.15), var(--sheet-accent));
    color:#050505;
    transform:translateY(-2px);
    box-shadow:0 18px 26px rgba(0,0,0,.35);
    outline:none;
  }
  .desk-subitem:hover::after,
  .desk-subitem:focus-visible::after{
    border-color:rgba(255,255,255,.2);
  }

  .desk-notch{
    position:fixed;
    top:calc(var(--gutter) + 6px);
    right:var(--gutter);
    width:48px;
    height:48px;
    border-radius:999px;
    border:1px solid rgba(255,255,255,.25);
    background:rgba(0,0,0,.6);
    display:flex;
    align-items:center;
    justify-content:center;
    color:var(--brand-white);
    z-index:47;
    opacity:0;
    pointer-events:none;
    transition:opacity .3s ease, transform .3s ease, border-color .3s ease;
