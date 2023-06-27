import React from 'react';
import "./navbar.css";
import image from "../src/photos/football.svg";

const Navbar = () => {
    return(
        <div>
            <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#"><img src={image} alt="" width="45" height="37"></img></a>
                    <a class="navbar-brand position-absolute top-50 start-50 translate-middle" href="#">Football</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                            <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="/">Home</a>
                            </li>
                            <li class="nav-item">
                            <a class="nav-link active" href="/">Features</a>
                            </li>
                            <li class="nav-item">
                            <a class="nav-link active" href="/data">Data</a>
                            </li>
                            <li class="nav-item">
                            <a class="nav-link active" href="/" tabindex="-1" aria-disabled="true">Shop</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </div>
    )
}

export default Navbar;