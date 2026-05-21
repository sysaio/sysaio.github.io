# 🏡 Apartmán u Micky - Stylové ubytování Moravské Toskánsko 🍷

Stylové ubytování v klidné lokalitě jižní Moravy.
Ideální pro rodiny, přátele i menší skupiny.

👉 Kapacita až 6 osob | 70 m²

## Hodnocení

<a href="https://search.google.com/local/writereview?placeid=ChIJ1U1OUQAnE0cR8a7K8JJisHw"
   target="_blank"
   rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/Google-Napsat%20recenzi-blue?logo=google"
       alt="Google Reviews">
</a>

<a href="https://search.google.com/local/writereview?placeid=ChIJ1U1OUQAnE0cR8a7K8JJisHw"
   target="_blank"
   rel="noopener noreferrer">
   👉 Napsat recenzi na Google Maps
</a>

---

## 💰 Ceník ubytování

| Počet osob | Cena za apartmán / noc | Cena za osobu |
|---|---:|---:|
| 1 osoba | 1 700 Kč | 1 700 Kč |
| 2 osoby | 1 900 Kč | 950 Kč |
| 3 osoby | 2 100 Kč | 700 Kč |
| 4 osoby | 2 300 Kč | 575 Kč |
| 5 osob | 2 500 Kč | 500 Kč |
| 6 osob | 2 700 Kč | 450 Kč |

🥐 Snídaně v ceně
👶 Jedno dítě do 3 let zdarma
📶 Wi-Fi a parkování zdarma
📌 Uvedené ceny jsou konečné včetně DPH

## 🛏️ Dispozice apartmánu

- vstupní chodba
- koupelna (pračka + sušička)
- samostatné WC
- plně vybavená kuchyně
- jídelna s obývacím prostorem
  - rozkládací gauč
- prostorná ložnice
  - 1× manželská postel
  - 2× samostatné postele

---

## 🍷 Možnosti navíc

- polopenze / plná penze
- řízená degustace vín
- grilování
- víkendové pobyty

---

## 📞 Kontakt a rezervace

📧 kocian.libor@seznam.cz
📱 +420 602 941 181

🕒 Check-in: 15:00–22:00

💡 Nejlepší cena při přímé rezervaci telefonicky nebo e-mailem.


## 📍 Adresa: Hradčany 390, 696 13 Šardice

📌 **Mapy:**

<!-- Badge odkazy -->
<a href="https://maps.app.goo.gl/unh45Vpv856czuGMA" target="_blank" rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/Google%20Maps-Otevřít%20mapu-green?logo=googlemaps" alt="Google Maps">
</a>

<a href="https://mapy.com/s/cesakosebo" target="_blank" rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/Mapy.cz-Navigace-blue" alt="Mapy.cz">
</a>

<!-- Minimapka -->
<iframe style="border:none" src="https://mapy.com/s/motakevova" width="400" height="280" frameborder="0"></iframe>

<!-- Textové odkazy -->
- 🗺️ <a href="https://maps.app.goo.gl/unh45Vpv856czuGMA" target="_blank" rel="noopener noreferrer">
  Google Maps – Ubytování u Micky
</a>

- 🌍 <a href="https://mapy.com/s/cesakosebo" target="_blank" rel="noopener noreferrer">
  Mapy.com – navigace
</a>

---

## 📸 Fotogalerie Apartmán u Micky Šardice 390

<div class="gallery">

<button onclick="prevImage()">❮</button>

<img id="gallery-image" src="../images/ap01.jpeg">

<button onclick="nextImage()">❯</button>

</div>

<script>

const images = [
  "../images/ap01.jpeg",
  "../images/ap02.jpeg",
  "../images/ap03.jpeg",
  "../images/ap04.jpeg",
  "../images/ap05.jpeg",
  "../images/ap06.jpeg",
  "../images/ap07.jpeg",
  "../images/ap08.jpeg",
  "../images/ap09.jpeg",
  "../images/ap10.jpeg",
  "../images/ap11.jpeg",
  "../images/ap12.jpeg",
  "../images/ap13.jpeg",
  "../images/ap14.jpeg",
  "../images/ap15.jpeg",
  "../images/ap16.jpeg",
  "../images/ap17.jpeg",
  "../images/ap18.jpeg",
  "../images/ap19.jpeg",
  "../images/ap20.jpeg"
];

let current = 0;

const img = document.getElementById("gallery-image");

function showImage() {
  img.src = images[current];
}

function nextImage() {
  current = (current + 1) % images.length;
  showImage();
}

function prevImage() {
  current = (current - 1 + images.length) % images.length;
  showImage();
}

let startX = 0;

img.addEventListener("touchstart", e => {
  startX = e.touches[0].clientX;
}, { passive: true });

img.addEventListener("touchmove", e => {
  e.preventDefault();
}, { passive: false });

img.addEventListener("touchend", e => {

  let endX = e.changedTouches[0].clientX;

  if (startX - endX > 50) {
    nextImage();
  }

  if (endX - startX > 50) {
    prevImage();
  }

}, { passive: true });

</script>

<style>

.gallery {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;
}

.gallery img {
  width: 90%;
  max-width: 800px;
  border-radius: 12px;
  touch-action: none;
  user-select: none;
}

.gallery button {
  font-size: 2em;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0 10px;
}

</style>
