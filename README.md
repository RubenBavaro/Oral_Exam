<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the RANDOM STUDENT SELECTION project.
*** If you have any suggestions to improve the project or the README, please fork the repo and create a pull request,
*** or simply open an issue with your ideas. Happy coding!
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://rubenbavaro.github.io/Oral_Exam/">
    <img src="static/img/logo.jpg" alt="Oral Exam Random Student Logo" width="150" height="150">
  </a>

  <h3 align="center">Oral Exam Random Student</h3>

  <p align="center">
    A web page to display a class roster and randomly select students for oral examinations in real-time. Made for the 4ITIA-A classroom specificaly of the Panetti-Pitagora school.
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#built-with">Built With</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

**Oral Exam Random Student** is a web application designed to manage and facilitate classroom oral examinations by randomly selecting students.  
This page displays the complete list of students in a class, and by clicking the provided button, it triggers an API call (developed by the me using fastapi) that randomly selects the students to be interrogated, displaying the results in real-time.  
The system helps ensure that the selection process is both transparent and fair.

<!-- USAGE -->
## Usage

- **Access:**  
  Visit the live page at:  
  [Oral Exam Random Students](https://rubenbavaro.github.io/Oral_Exam/)

- **Triggering the Selection:**  
  Click the button to initiate the random selection.  
  The API will randomly choose one or more students for the oral exam and immediately display the selected results on the page.

- **Real-Time Updates:**  
  Each click initiates a new API request, ensuring that fresh selection results are generated every time, making the process dynamic and fair.

<!-- BUILT WITH -->
## Built With

This project is built using:
* **HTML5** – For structuring the content.
* **CSS** – For styling and layout of the interface.
* **JavaScript** – For handling user interactions and managing API calls.
* **Fetch API** – To perform GET requests to the server and retrieve data in real-time.
*  **Python** – The server-side application logic is written in Python, which powers data handling, business logic, and integration with external services. Python's versatility and extensive standard library support make it a great choice for developing scalable and maintainable backend code.
* **FastAPI** – A modern, high-performance web framework for building APIs with Python 3.6+ based on standard Python type hints. FastAPI is used to create RESTful API endpoints, offering automatic data validation, asynchronous request handling, and interactive API documentation (using Swagger UI), thereby simplifying development and testing.

---

Feel free to explore the project and contribute with improvements or additional features!
