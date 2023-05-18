<p align="center">
  <a href="https://mauricekuenicke.github.io/calpyso/"><img src="docs/assets/logo/svg/Color logo - no background.svg" alt="Calypso" width="60%"></a>
</p>

<p align="center">
    <em>A user authentication microservice implementation</em>
</p>

<p align="center">
<a href="https://github.com/MauriceKuenicke/calypso/actions/workflows/cicd.yml?query=workflow%3ACICD+branch%3Amain++" target="_blank">
    <img src="https://github.com/MauriceKuenicke/calypso/actions/workflows/cicd.yml/badge.svg?branch=main" alt="Test">
</a>
<a href="https://codecov.io/gh/MauriceKuenicke/calypso" > 
    <img src="https://codecov.io/gh/MauriceKuenicke/calypso/branch/main/graph/badge.svg?token=NYH162MDJD"/> 
</a>
</p>

---

**Documentation**: <a href="https://mauricekuenicke.github.io/calypso/" target="_blank">https://mauricekuenicke.github.io/calypso/</a>

**Source Code**: <a href="https://github.com/MauriceKuenicke/calypso" target="_blank">https://github.com/MauriceKuenicke/calypso</a>

---
<p align="center">
<em>A moon of Saturn named after the nymph who held Odysseus captive on her island in Greek mythology. Most famously known for her role in Homer's epic poem "The Odyssey." When the Greek hero Odysseus became stranded on her island after a shipwreck, Calypso fell in love with him and kept him as her captive for seven years, promising him immortality and eternal youth if he stayed with her. Calypso is often seen as a symbol of temptation and the dangers of the sea, and her story is frequently retold in literature, music, and art.</em> - chatGPT</p>

Securely manage user authentication with a simple API interface. Lightweight, scalable, and customizable for small to medium-sized apps. Integrate with ease and free your application from complex authentication frameworks.

---
# ⚠️ Important
This project is currently not safe for use in a production environment. Use at your own risk.


# Local Database Setup
You can run a local Postgres database using Docker. All you need is Docker installed + the latest official Postgres image.
```sh
docker run --name CalypsoDB -e POSTGRES_PASSWORD=admin -e POSTGRES_DB=calypso -e POSTGRES_USER=admin -p 5432:5432 -d postgres
```