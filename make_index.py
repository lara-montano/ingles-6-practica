import re, sys, os
# Genera index.html (portada de GitHub Pages). Uso: python3 make_index.py  (desde la raiz del repo)
# Edita las listas SIMS / GYM / EPS de abajo cuando agregues material y vuelve a correrlo.
R = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.join(R, "04_Simuladores_web")
# sello de autoría: copiado byte a byte del simulador de referencia
tpl = open(f"{WEB}/U2_G7_reported_speech.html", encoding="utf-8").read()
i = tpl.index("<!-- ============ Sello de autoría"); j = tpl.index("</script>", i) + len("</script>")
SELLO = tpl[i:j]

SIMS = [
 ("u1","Unit 1 · Grammar 1","Conditionals","Types 0–3, mixed conditionals, formal inversion and the comma rule.","U1_G1_conditionals.html"),
 ("u1","Unit 1 · Grammar 2","Wish, if only & would rather","Talking about the unreal: wish + past / past perfect / would, if only, would rather, it's time.","U1_G2_wish_would_rather.html"),
 ("u1","Unit 1 · Grammar 3","Conditional linkers","unless · as long as · provided that · in case · once · even if · whether…or not.","U1_G3_conditional_linkers.html"),
 ("u1","Unit 1 · Grammar 4","The passive","Active ↔ passive in every tense, by/with, get-passive, <i>It is said that…</i>","U1_G4_passive.html"),
 ("u2","Unit 2 · Grammar 5","Past modals of deduction","must have · might have · can't have + participle, with a certainty thermometer.","U2_G5_past_modals.html"),
 ("u2","Unit 2 · Grammar 6","Verb + object + infinitive","want / ask / tell somebody to do… and the exceptions: make, let, help, suggest, prevent from.","U2_G6_verb_object_infinitive.html"),
 ("u2","Unit 2 · Grammar 7","Reported speech","Backshift, say/tell, time and place words, reported questions and commands.","U2_G7_reported_speech.html"),
 ("u2","Unit 2 · Grammar 8","Relative clauses","Defining vs non-defining, the comma switch, who / which / that / whose / where / when.","U2_G8_relative_clauses.html"),
 ("u3","Unit 3 · Grammar 9","Noun clauses","Clauses as subject or object: that / wh- / whether, statement word order, <i>What we need is…</i>","U3_G9_noun_clauses.html"),
 ("u3","Unit 3 · Grammar 10","Future forms for predictions","will / going to / might, future continuous and future perfect on a certainty thermometer and a timeline.","U3_G10_future_forms.html"),
 ("u4","Unit 4 · Grammar 11","The gerund after a preposition","interested in working, instead of buying, and the <i>look forward to</i> trap.","U4_G11_gerund_after_preposition.html"),
 ("u4","Unit 4 · Grammar 12","The future passive","will be + participle: recycled materials will be used. When to name the doer.","U4_G12_future_passive.html"),
 ("u5","Unit 5 · Grammar 13","The future in the past","was going to · would · was supposed to · was about to: the plans we never kept.","U5_G13_future_in_the_past.html"),
 ("u5","Unit 5 · Grammar 14","The future progressive","will be + -ing: an action in progress at a future moment, on a timeline.","U5_G14_future_progressive.html"),
]
GYM = {1:"5:36",2:"4:56",3:"4:49",4:"3:58",5:"3:57",6:"4:01",7:"3:59",8:"3:01",9:"3:19",10:"3:06",11:"3:46",12:"3:48",13:"3:52",14:"3:49",15:"4:01",16:"4:05",17:"3:45",18:"4:21",19:"4:25",20:"3:55"}
BLOCKS = [
 ("Core block · sesiones 1–3 · contexto, detalles y sonidos parecidos · se oyen dos veces · 15 s para responder", range(1,4)),
 ("Sesiones 4–7 · negativos, deducción y funciones · una escucha · 15 s", range(4,8)),
 ("Sesiones 8–10 · condicionales, idioms y mixto · una escucha · 10 s", range(8,11)),
 ("Advanced block · sesiones 11–17 · números, referentes, causativos, respuestas, verbos e idioms difíciles, comparaciones · una escucha · 10 s", range(11,18)),
 ("Sesiones 18–19 · conversación larga y minilectures · una escucha · 12 s", range(18,20)),
 ("Sesión 20 · final boss: todo, sabor C1 · una escucha · 10 s", range(20,21)),
]
EPS = [
 ("E1","The Magnet in Your Kitchen Door","Unit 6 · magnetismo","5:02","E1_U6_magnetism_tts.m4a","transcripts_E1-E5.pdf"),
 ("E2","Congratulations, You Helped Ruin a Small Town","Unit 7 · sobreturismo","5:03","E2_U7_overtourism_tts.m4a","transcripts_E1-E5.pdf"),
 ("E3","The Man Who Noticed the Door","Unit 8 · futuro del trabajo","4:48","E3_U8_future_work_tts.m4a","transcripts_E1-E5.pdf"),
 ("E4","Word Detectives","Unit 9 · palabras nuevas y moda","5:20","E4_U9_words_fashion_tts.m4a","transcripts_E1-E5.pdf"),
 ("E5","One Now or Two Later","Unit 10 · procrastinación","4:44","E5_U10_procrastination_tts.m4a","transcripts_E1-E5.pdf"),
 ("E6","The Vault at the End of the World","Grammar 3 · Structure 2 · conjunciones condicionales y formación de palabras","5:09","E6_G3-S2_seed_vault_tts.m4a","e6_transcript.pdf"),
]
def sim_cards():
    return "\n".join(f'    <a class="sim {u}" href="04_Simuladores_web/{f}"><div class="unit">{k}</div><h3>{t}</h3><p>{d}</p><span class="go">Abrir →</span></a>' for u,k,t,d,f in SIMS)
def gym_rows():
    out=[]
    for label, rng in BLOCKS:
        out.append(f'    <div class="block">{label}</div>\n    <ul class="rows">')
        for n in rng:
            out.append(f'      <li class="row"><div><div class="t">Sesión {n:02d}</div><div class="d">{GYM[n]} · 8 reactivos · <a class="lnk" href="02_SELLI_Gym/audio/selli_gym_S{n:02d}.m4a" download>descargar</a></div></div><audio controls preload="none" src="02_SELLI_Gym/audio/selli_gym_S{n:02d}.m4a"></audio></li>')
        out.append('    </ul>')
    return "\n".join(out)
def ep_rows():
    return "\n".join(f'      <li class="row"><div><div class="t">{e} · {t}</div><div class="d">{u} · {d} · <a class="lnk" href="03_Listening_Lab/transcripts/{tr}" target="_blank" rel="noopener">transcript</a> · <a class="lnk" href="03_Listening_Lab/episodios/{f}" download>descargar</a></div></div><audio controls preload="none" src="03_Listening_Lab/episodios/{f}"></audio></li>' for e,t,u,d,f,tr in EPS)

html = f"""<!DOCTYPE html>
<!-- =====================================================================
  INGLÉS 6 · Material de práctica (B1+) · página de inicio del sitio
  Autor: Prof. Daniel Lara · Instagram y Google Scholar: profe.daniellara
  No elimines los créditos.
====================================================================== -->
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="author" content="Prof. Daniel Lara (@profe.daniellara)">
<meta name="copyright" content="© Prof. Daniel Lara — Instagram/Google Scholar: profe.daniellara">
<title>Inglés 6 · Práctica · Prof. Daniel Lara</title>
<style>
  :root{{
    --navy:#1F3A5F; --navydark:#142741; --navylt:#E8ECF3;
    --green:#1F7A4D; --teal:#0E7C7B; --indigo:#3A3A8C; --wine:#8C2F53; --purple:#6A2C91;
    --grammar:#D9761A; --grammarlt:#FBEEDF;
    --ink:#262626; --soft:#F4F6F5; --rule:#CBD3CE;
  }}
  *{{box-sizing:border-box;margin:0;padding:0}}
  html{{-webkit-text-size-adjust:100%;scroll-behavior:smooth}}
  body{{font-family:Lato,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--ink);background:var(--soft);line-height:1.55}}
  header{{background:linear-gradient(135deg,var(--navy),var(--navydark));color:#fff;padding:26px 20px 22px;position:relative;overflow:hidden}}
  header .deco{{position:absolute;right:16px;top:-14px;font-size:118px;opacity:.12;pointer-events:none}}
  .wrap{{max-width:1000px;margin:0 auto;padding:0 14px 90px}}
  header .wrap{{padding-bottom:0}}
  .kicker{{font-size:12px;letter-spacing:.13em;font-weight:800;color:#BFD3EE;text-transform:uppercase}}
  header h1{{font-size:clamp(24px,4.6vw,36px);margin:4px 0 4px;font-weight:900}}
  header .sub{{color:#D6E1F0;font-size:clamp(13px,2.3vw,16px);max-width:720px}}
  .chipline{{margin-top:10px;display:flex;gap:6px;flex-wrap:wrap}}
  .chipline a,.chipline span{{background:rgba(255,255,255,.16);border-radius:999px;padding:4px 12px;font-size:12px;font-weight:700;color:#fff;text-decoration:none}}
  .chipline a:hover{{background:rgba(255,255,255,.28)}}
  nav{{position:sticky;top:0;z-index:5;background:#fff;border-bottom:1px solid var(--rule);box-shadow:0 1px 4px rgba(0,0,0,.05)}}
  nav .wrap{{display:flex;gap:4px;flex-wrap:wrap;padding:6px 14px}}
  nav a{{color:var(--navy);text-decoration:none;font-weight:800;font-size:14px;padding:8px 12px;border-radius:9px}}
  nav a:hover{{background:var(--navylt)}}
  main{{padding-top:18px}}
  section{{margin-bottom:26px;scroll-margin-top:60px}}
  section>h2{{font-size:22px;color:var(--navydark);margin-bottom:4px}}
  section>p.lead{{color:#555;font-size:15px;margin-bottom:12px}}
  .card{{background:#fff;border:1px solid var(--rule);border-radius:14px;padding:16px 18px;margin-bottom:14px;box-shadow:0 1px 4px rgba(0,0,0,.05)}}
  .card h3{{font-size:17px;color:var(--navydark);margin-bottom:4px}}
  .muted{{color:#666;font-size:14px}}
  .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px}}
  .sim{{display:block;background:#fff;border:1px solid var(--rule);border-left:6px solid var(--green);border-radius:12px;padding:14px 16px;text-decoration:none;color:var(--ink);box-shadow:0 1px 4px rgba(0,0,0,.05);transition:transform .12s,box-shadow .12s}}
  .sim:hover{{transform:translateY(-2px);box-shadow:0 4px 12px rgba(0,0,0,.09)}}
  .sim.u1{{border-left-color:var(--green)}} .sim.u2{{border-left-color:var(--teal)}} .sim.u3{{border-left-color:var(--indigo)}} .sim.u4{{border-left-color:var(--wine)}} .sim.u5{{border-left-color:var(--purple)}}
  .sim .unit{{font-size:11px;font-weight:900;letter-spacing:.08em;text-transform:uppercase;color:#777}}
  .sim.u1 .unit{{color:var(--green)}} .sim.u2 .unit{{color:var(--teal)}} .sim.u3 .unit{{color:var(--indigo)}} .sim.u4 .unit{{color:var(--wine)}} .sim.u5 .unit{{color:var(--purple)}}
  .sim h3{{font-size:16px;margin:2px 0 4px;color:var(--navydark)}}
  .sim p{{font-size:13.5px;color:#555}}
  .sim .go{{display:inline-block;margin-top:8px;font-weight:800;font-size:13px;color:var(--grammar)}}
  .btns{{display:flex;gap:8px;flex-wrap:wrap;margin:8px 0 6px}}
  .btn{{display:inline-block;border:0;border-radius:10px;padding:9px 14px;font:800 14px Lato,sans-serif;text-decoration:none;color:#fff;background:var(--navy);cursor:pointer}}
  .btn.ghost{{background:#fff;color:var(--navy);border:2px solid var(--navy)}}
  .rows{{list-style:none}}
  .row{{display:grid;grid-template-columns:1fr auto;gap:6px 12px;align-items:center;padding:9px 0;border-top:1px solid var(--rule)}}
  .row:first-child{{border-top:0}}
  .row .t{{font-weight:800;font-size:14.5px}}
  .row .d{{font-size:12.5px;color:#777}}
  .row audio{{width:100%;max-width:340px;height:36px}}
  .lnk{{font-weight:800;color:var(--navy);text-decoration:none}}
  .block{{font-size:12px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;color:var(--grammar);margin:14px 0 2px}}
  .tip{{background:var(--grammarlt);border-left:4px solid var(--grammar);border-radius:8px;padding:10px 12px;font-size:14px;margin-top:12px}}
  footer.credits{{text-align:center;color:#666;font-size:13px;padding:22px 14px 0}}
  footer.credits a{{color:var(--navy);font-weight:700}}
  @media(max-width:560px){{.row{{grid-template-columns:1fr}}.row audio{{max-width:100%}}}}
</style>
</head>
<body>
<header>
  <div class="deco">🎧</div>
  <div class="wrap">
    <div class="kicker">Inglés 6 · B1+</div>
    <h1>Material de práctica</h1>
    <p class="sub">Simuladores de gramática, simulacro tipo SELLI, el SELLI Gym de listening y el Listening Lab con los episodios de <i>In the Lab FM</i>. Todo se abre desde aquí y los audios se reproducen sin descargar.</p>
    <div class="chipline">
      <span>Prof. Daniel Lara</span>
      <a href="https://www.instagram.com/profe.daniellara/" target="_blank" rel="noopener">Instagram @profe.daniellara</a>
      <a href="https://scholar.google.com/citations?user=ifG2_hwAAAAJ" target="_blank" rel="noopener">Google Scholar</a>
      <a href="https://github.com/lara-montano/ingles-6-practica" target="_blank" rel="noopener">Descargar todo (GitHub)</a>
    </div>
  </div>
</header>
<nav><div class="wrap">
  <a href="#simuladores">🧪 Simuladores</a><a href="#mock">📝 SELLI Mock</a><a href="#gym">🏋️ SELLI Gym</a><a href="#lab">🎧 Listening Lab</a>
</div></nav>
<main class="wrap">

<section id="simuladores">
  <h2>Simuladores de gramática</h2>
  <p class="lead">Una página por tema del manual. Tres modos: <b>Explore</b> (la regla en acción) → <b>Build</b> (arma oraciones) → <b>Drill</b> (práctica graduada ★ ★★ ★★★ con marcador y racha). Funcionan sin internet: puedes guardar la página en tu teléfono.</p>
  <div class="grid">
{sim_cards()}
  </div>
</section>

<section id="mock">
  <h2>SELLI Mock · Units 1–2</h2>
  <p class="lead">Simulacro de práctica en formato SELLI restringido a las Units 1–2: 70 reactivos, 75 minutos. No cuenta para la calificación; sirve para ver qué fila del perfil sale baja.</p>
  <div class="card">
    <h3>Cómo se aplica</h3>
    <p class="muted">Parte I (Listening, 16 reactivos): reproduce el audio <b>una sola vez y sin pausar</b>; trae las instrucciones, el ejemplo y 12 segundos de respuesta por reactivo. Después resuelve las Partes II–IV (Structure 20 · Vocabulary 14 · Reading 20) en unos 60 minutos y llena la hoja de perfil del final.</p>
    <div class="btns"><a class="btn" href="01_SELLI_Mock_U1-U2/mock6_examen.pdf" target="_blank" rel="noopener">📄 Cuadernillo (PDF, 10 págs.)</a><a class="btn ghost" href="01_SELLI_Mock_U1-U2/mock6_listening.m4a" download>⬇️ Descargar el audio</a></div>
    <ul class="rows"><li class="row"><div><div class="t">Parte I · Listening</div><div class="d">10:30 · instrucciones + 16 reactivos con sus pausas</div></div><audio controls preload="none" src="01_SELLI_Mock_U1-U2/mock6_listening.m4a"></audio></li></ul>
  </div>
</section>

<section id="gym">
  <h2>SELLI Gym</h2>
  <p class="lead">20 sesiones de listening en formato SELLI/ITP: 8 reactivos cada una, 160 en total. Una sesión por día. Lee las cuatro opciones <b>antes</b> de darle play; el audio corre solo (numera, habla, pregunta y deja los segundos de respuesta).</p>
  <div class="card">
    <div class="btns"><a class="btn" href="02_SELLI_Gym/selli_gym.pdf" target="_blank" rel="noopener">📄 Cuadernillo del Gym (PDF, 21 págs.)</a></div>
{gym_rows()}
    <div class="tip"><b>Reglas de oro.</b> Lee las opciones antes; la correcta casi siempre parafrasea y las incorrectas repiten palabras del audio; un negativo o un idiom puede voltear el sentido; nunca dejes un reactivo en blanco.</div>
  </div>
</section>

<section id="lab">
  <h2>The Listening Lab · <i>In the Lab FM</i></h2>
  <p class="lead">Cada episodio se escucha <b>dos veces</b>: primero por la idea general, luego con la tarea de la ficha. El transcript se abre <b>después</b> de la segunda escucha.</p>
  <div class="card">
    <div class="btns"><a class="btn" href="03_Listening_Lab/listening_lab.pdf" target="_blank" rel="noopener">📄 Fichas de listening (PDF, 8 págs.)</a><a class="btn" href="03_Listening_Lab/cuestionarios.pdf" target="_blank" rel="noopener">📄 Cuestionarios de los episodios (PDF, 11 págs.)</a></div>
    <ul class="rows">
{ep_rows()}
    </ul>
    <div class="block">Lectura del manual leída en voz alta</div>
    <ul class="rows">
      <li class="row"><div><div class="t">Unit 2 · Reading 3 · Four Trips That Went Sideways</div><div class="d">2:53 · sigue el texto del manual mientras escuchas · <a class="lnk" href="03_Listening_Lab/lecturas/U2_R3_Four_Trips_That_Went_Sideways.m4a" download>descargar</a></div></div><audio controls preload="none" src="03_Listening_Lab/lecturas/U2_R3_Four_Trips_That_Went_Sideways.m4a"></audio></li>
    </ul>
  </div>
</section>

</main>
<footer class="credits">
  Material creado por <b>Prof. Daniel Lara</b> ·
  <a href="https://www.instagram.com/profe.daniellara/" target="_blank" rel="noopener">Instagram @profe.daniellara</a> ·
  <a href="https://scholar.google.com/citations?user=ifG2_hwAAAAJ" target="_blank" rel="noopener">Google Scholar</a><br>
  Inglés 6 · B1+ · © 2026 · Si lo compartes, conserva la atribución.
</footer>

{SELLO}
</body>
</html>
"""
open(f"{R}/index.html","w",encoding="utf-8").write(html)
print("index.html:", len(html), "bytes; sello:", "credito-profe-daniellara" in SELLO)
