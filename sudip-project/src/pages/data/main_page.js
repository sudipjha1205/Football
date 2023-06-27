import React from 'react';
import { useState,useEffect } from 'react';
import Navbar from '../../navbar';
import Data_Tab from '../../components/data_tab';

const Data = () => {
    return(
        <div>
            <Navbar /> 
            <Data_Tab />
        </div>
    )
}

export default Data;