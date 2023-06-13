import React from "react";
import "./cards.css";

import vinicius from "../../photos/vinicius.jpg";
import messi from "../../photos/messi.jpg";
import city from "../../photos/city.jpg";
import haaland from "../../photos/haaland.jpg";
import dortmund from "../../photos/dortmund.jpeg";
import juventus from "../../photos/juventus.jpeg";
import mourinho from "../../photos/mourinho.jpeg";
import best from "../../photos/best_signing.jpeg";

const Cards = () => {

    const first_row = [
        {img_src:city, heading:"Is this Manchester city team the best in PL history?"},
        {img_src:messi, heading:"Messi leading the race for Ballon D'Or"},
        {img_src:vinicius, heading:"Vincius wars against racism"},
        {img_src:haaland, heading:"The Machine"}
    ]

    const first_row_content = first_row.map((post) =>
        <div class="col-md-3">
            <div class="card text-white bg-secondary mb-3" style={{ width: '100%', height: '100%' }}>
                <img src={post.img_src} class="card-img-top" alt="..." style={{ width: '100%', height: '100%' }}></img>
                <div class="card-body">
                    <p class="card-text">{post.heading}</p>
                </div>
            </div>
        </div> 
    )

    const second_row = [
        {img_src:dortmund, heading:"Dortmund one step away from it's first bundesliga in 10 years"},
        {img_src:juventus, heading:"Juventus handed a 10 points reduction"},
        {img_src:mourinho, heading:"Can Mourinho lead Roma to it's consecutive european glory?"},
        {img_src:best, heading:"The 20 best signing of this season"}
    ]

    const second_row_content = second_row.map((post) =>
        <div class="col-md-3">
            <div class="card text-white bg-secondary mb-3 hover-pointer" style={{ width: '100%', height: '100%' }}>
                <img src={post.img_src} class="card-img-top" alt="..." style={{ width: '100%', height: '100%' }}></img>
                <div class="card-body">
                    <p class="card-text">{post.heading}</p>
                </div>
            </div>
        </div> 
    )

    return(
        <div class="container-fluid">
            <h2 class="border border-light border-2 text-light m-1 p-1 w-100% d-flex justify-content-center">Latest</h2>
            <div class="col-12 row m-0 p-0 d-flex g-4">
                {first_row_content}
            </div>    
            <br></br>
            <div class="col-12 row m-0 p-0 d-flex g-4">
                {second_row_content}
            </div>
        </div>
    )
}

export default Cards;