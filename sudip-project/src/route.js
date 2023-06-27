import React from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Data from "../src/pages/data/main_page";
import Homepage from './pages/homepage';
//import history from './history';

const Route_file = () => {
    return(
        <BrowserRouter>
            <Routes >
                <Route path="/" element={<Homepage/>} />
                <Route path="/data" element={<Data/>} />
            </Routes>
        </BrowserRouter>
    )
}

export default Route_file;