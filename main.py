<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>CV - Template</title>
  <meta name="description" content="simple CV example created with HTML and CSS">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.13/css/all.css" integrity="sha384-DNOHZ68U8hZfKXOrtjWvjxusGo9WQnrNx2sqG0tfsghAvtVlRW3tvkXWZh58N9jp" crossorigin="anonymous">
  <link rel="stylesheet" href="style.css">
</head>

<body>
  <header>
    <div>
      <img src="./img/avatar.jpg" />
    </div>
    <h1> Amreena Akhtar</h1>
    <section>
      <p>I am an undergraduate student .</p>

    </section>
  </header>
  <main>
    <section>
      <h3>Courses & Workshops</h3>
      <article class='course'>
        <div class='title'>
          <h4>Udacity: Intro to HTML and CSS</h4>
        </div>
        <div class="descrition">
          <p>Build styled, well-structured websites. Learn how to use HTML5 standard to create websites. Understand CSS syntax, selectors, and units. Learn about code editors and a browser's Developer Tools.</p>
        </div>
      </article>
      <article class='course'>
        <div class='title'>
          <h4>Udemy: The Web Developer Bootcamp</h4>
        </div>
        <div class="descrition">
          <p>Learn how to create full-stack web applications from scratch using HTML, CSS, JavaScript, jQuery, VanillaJS, NodeJS, MongoDB.</p>
        </div>
      </article>
      <article class='course'>
        <div class='title'>
          <h4>EdX: Web Programming with JavaScript</h4>
        </div>
        <div class="descrition">
          <p>Learn how to create web apps and prototypes with JavaScript, represent and exchange data using JavaScript Object Notation (JSON), and how to access RESTful APIs on the web.</p>
        </div>
      </article>
      <article class='course'>
        <div class='title'>
          <h4>Django Girls: 2-Day Workshops</h4>
        </div>
        <div class="descrition">
          <p>Learn back-end development with simple blog application using Django  framework.</p>
        </div>
      </article>
    </section>
    <section>
      <h3>Skills</h3>
      <div class='skills'>
        <div class='column'>
          <h4>Good knowledge</h4>
          <ul>
            <li>HTML5</li>
            <li>CSS</li>
            <li>JavaScript ES5/6</li>
            <li>SQL</li>
          </ul>
        </div>
        <div class='column'>
          <h4>Basic knowledge</h4>
          <ul>
            <li>jQuery</li>
            <li>NodeJS</li>
            <li>MongoDB</li>
            <li>Django</li>
          </ul>
        </div>
        <div>
          <h4>Languages</h4>
          <p>🇵🇱 Urdu - Native speaker</p>
          <p>🇬🇧 English - Proficient C1/C2</p>

        </div>
      </div>
    </section>

    <section>
      <h3>Education</h3>
      <article>
        <div class='school'>
          <span>2017-2019</span> <strong>Sesame street school,Rwp</strong>
        </div>
        <div class="descrition">
          Bechelor Degree of software engineering
        </div>
      </article>
      <article>
        <div class='school'>
          <span>2012-2015</span> <strong>Underwater kittens high school</strong>
        </div>
        <div>
          Main subject: Cathemathics
        </div>
      </article>
    </section>
    <section>
      <h3>Experience</h3>
      <article>
        <div class='job-title'>
          <span>03.2018 - 06.2018</span> <strong>Tentacles Company</strong><br> <strong>Position:</strong> Web developer Intern
        </div>
        <div>
          <p><strong>Tech stack:</strong> HTML5 / CSS / JavaScript / jQuery</p>
          <ul class="job-description">
            <li>Develop web application for Octopoda departments</li>
            <li>Implement UI (front-end site) based on received graphic design and requirements</li>
            <li>Co-operate with the back-end team </li>
          </ul>
        </div>
      </article>
    </section>
  </main>
</body>
</html>
