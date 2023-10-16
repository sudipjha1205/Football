import React from 'react';
import { useState, useEffect, useCallback, memo } from 'react';

import { GrPrevious } from 'react-icons/gr';
import { GrCaretNext } from 'react-icons/gr';
import { GrNext } from 'react-icons/gr';

import './attack.css';

const Goalie = (props) => {

    const [goalie, setGoalie] = useState([]);
    const [start, setStart] = useState(0);
    const [end,setEnd] = useState(10);
    const [searchText, setSearchText] = useState('');
    const [clicked, setClicked] = useState(0);
    const [drop, setDrop] = useState(0);

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/api/${props.league}/players/goalie/`)
           .then((response) => response.json())
           .then((data) => {
              setGoalie(data);
           });
    },[]);

    const render_table = () => {
        console.log(searchText);
        const index = goalie.findIndex((player) => (player.player).toLowerCase() === (searchText).toLowerCase());
        if (index == -1){
            
        } else {
            setStart(index - 4);
            setEnd(index + 6);
        }
    }

    useEffect(() => {
        render_table();
    },[clicked])


    const goalie_table = goalie && goalie.slice(start,end).map((goalies) => 
        <tr>
        <th scope="row">{goalies.player}</th>
        <td>{goalies.nation}</td>
        <td>{goalies.squad}</td>
        <td>{goalies.age}</td>
        <td>{goalies.mp}</td>
        <td>{goalies.ga}</td>
        <td>{goalies.sota}</td>
        <td>{goalies.saves}</td>
        <td>{goalies.saveperc}</td>
        <td>{goalies.cs}</td>
        <td>{goalies.csperc}</td>
        <td>{goalies.pka}</td>
        <td>{goalies.pksv}</td>
        <td>{goalies.savepercpenalty}</td>
        </tr>
    )

    const increaseStart = (e) => {
        setStart(start + 10);
    }

    const decreaseStart = (e) => {
        setStart(start - 10);
    }

    const increaseEnd = (e) => {
        setEnd(end + 10);
    }

    const decreaseEnd = (e) => {
        setEnd(end - 10);
    }

    const onChange = (e) => {
        setSearchText(e.target.value);
    }

    const onClick = (e) => {
        setClicked(!clicked);
        setSearchText(e.target.innerText);
        setDrop(1);
    }

    const onClickButton = (e) => {
        e.preventDefault();
        setClicked(!clicked);
        setDrop(1);
    }

    return(
        <div>
            <div class="container">
                <div class="row align-items-center mt-3 mb-2">
                    <div class='col-3'>
                        <div class="badge text-wrap fs-5 m-1 p-1.5 b-2 fw-normal d-flex justify-content-start" onClick={() => {setEnd(10);setStart(0);setSearchText('')}}>
                            Goalie Standard Stats
                        </div>
                    </div>
                    <div class='col-3'>
                        <button class="btn btn-outline-secondary justify-content-start">Advance Stats</button>
                    </div>
                    <div class='col-6'>
                        <div class='d-flex justify-content-end'>
                            <form class="d-flex" onSubmit={onClickButton}>
                                <div class="container-fluid search-bar">
                                    <input class="form-control me-2" list="datalistOptions" value={searchText} type="search" placeholder="Search" aria-label="Search" onChange={onChange} onClick={() => {setDrop(0)}}></input>
                                    <div class='dropdown'  >
                                        {goalie.filter((item) => {
                                            const searchTyped = searchText.toLowerCase();
                                            const name = item.player.toLowerCase();

                                            return searchTyped && ( name.startsWith(searchTyped) || name.includes(searchTyped))
                                        }).map((item) => {  
                                            if (drop == 0){         
                                                return <div class="dropdown-row" onClick={onClick}>{item.player}</div>
                                            } else{
                                                return <div></div>
                                            }
                                        })}
                                    </div>
                                </div>
                                <button class="btn btn-outline-secondary" type="submit">Search</button>
                            </form>
                        </div>
                    </div>
                </div>
                <div class="table-style">
                    <table class="table table-secondary border-bottom border-rounded border-0.5 border-light table-hover fw-light">
                        <thead>
                            <tr>
                            <th scope="col">Player</th>
                            <th scope="col">Nation</th>
                            <th scope="col">Squad</th>
                            <th scope="col">Age</th>
                            <th scope="col">MP</th>
                            <th scope="col">GA</th>
                            <th scope="col">SOTA</th>
                            <th scope="col">Saves</th>
                            <th scope="col">Save %</th>
                            <th scope="col">CS</th>
                            <th scope="col">CS %</th>
                            <th scope='col'>PKA</th>
                            <th scope='col'>PK Save</th>
                            <th scope='col'>PKS %</th>
                            </tr>
                        </thead>
                        <tbody>
                            {goalie_table}
                        </tbody>
                    </table>
                </div>
                <p class="text-white-50">*Sorted by Tackles plus interception</p>
                <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                    { (start > 0) ?
                        (<button onClick={() => {decreaseEnd();decreaseStart();}} class="btn btn-outline-secondary" type='button' ><GrPrevious/></button>) :
                        (<button onClick={() => {decreaseEnd();decreaseStart();}} class="btn btn-outline-secondary disabled" type='button' ><GrPrevious/></button>)
                    }
                    { (end <= goalie.length ) ?
                        (<button onClick={() => {increaseEnd();increaseStart();}} class="btn btn-outline-secondary" type='button' ><GrNext/></button>) :
                        (<button onClick={() => {increaseEnd();increaseStart();}} class="btn btn-outline-secondary disabled" type='button' ><GrNext/></button>)
                    }
                </div>
                <hr class="white-line mt-5" />
            </div>
        </div>
    )
}

export default Goalie;