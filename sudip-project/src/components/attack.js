import React from 'react';
import { useState, useEffect, useCallback, memo } from 'react';

import { GrPrevious } from 'react-icons/gr';
import { GrCaretNext } from 'react-icons/gr';
import { GrNext } from 'react-icons/gr';

import './attack.css';

const Attack = (props) => {

    const [attacker, setAttacker] = useState([]);
    const [defender, setDefender] = useState([]);
    const [goalie, setGoalie] = useState([]);
    const [start, setStart] = useState(0);
    const [end,setEnd] = useState(10);
    const [searchText, setSearchText] = useState('');
    const [clicked, setClicked] = useState(0);
    const [drop, setDrop] = useState(0);

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/api/${props.league}/players/attack/`)
           .then((response) => response.json())
           .then((data) => {
              setAttacker(data);
           });
    },[]);

    const render_table = () => {
        console.log(searchText);
        const index = attacker.findIndex((player) => (player.player).toLowerCase() === (searchText).toLowerCase());
        if (index == -1){
            
        } else {
            setStart(index - 4);
            setEnd(index + 6);
        }
    }

    useEffect(() => {
        render_table();
    },[clicked])


    const attacker_table = attacker && attacker.slice(start,end).map((attackers) => 
        <tr>
        <th scope="row">{attackers.player}</th>
        <td>{attackers.nation}</td>
        <td>{attackers.pos}</td>
        <td>{attackers.squad}</td>
        <td>{attackers.age}</td>
        <td>{attackers.mp}</td>
        <td>{attackers.starts}</td>
        <td>{attackers.gls}</td>
        <td>{attackers.ast}</td>
        <td>{attackers.ga}</td>
        <td>{attackers.xg}</td>
        <td>{attackers.xag}</td>
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
                <div class="row align-items-center mt-5 mb-2">
                    <div class='col-3'>
                        <div class="badge text-wrap fs-5 m-1 p-1.5 b-2 fw-normal d-flex justify-content-start" onClick={() => {setEnd(10);setStart(0);setSearchText('')}}>
                            Offensive Standard Stats
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
                                        {attacker.filter((item) => {
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
                            <th scope="col">Pos</th>
                            <th scope="col">Squad</th>
                            <th scope="col">Age</th>
                            <th scope="col">MP</th>
                            <th scope="col">Starts</th>
                            <th scope="col">Goals</th>
                            <th scope="col">Assists</th>
                            <th scope="col">G+A</th>
                            <th scope="col">XG</th>
                            <th scope="col">XAG</th>
                            </tr>
                        </thead>
                        <tbody>
                            {attacker_table}
                        </tbody>
                    </table>
                </div>
                <p class="text-white-50">*Sorted by goals plus assists</p>
                <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                    { (start > 0) ?
                        (<button onClick={() => {decreaseEnd();decreaseStart();}} class="btn btn-outline-secondary" type='button' ><GrPrevious/></button>) :
                        (<button onClick={() => {decreaseEnd();decreaseStart();}} class="btn btn-outline-secondary disabled" type='button' ><GrPrevious/></button>)
                    }
                    { (end <= attacker.length ) ?
                        (<button onClick={() => {increaseEnd();increaseStart();}} class="btn btn-outline-secondary" type='button' ><GrNext/></button>) :
                        (<button onClick={() => {increaseEnd();increaseStart();}} class="btn btn-outline-secondary disabled" type='button' ><GrNext/></button>)
                    }
                </div>
                <hr class="white-line mt-5" />
            </div>
        </div>
    )
}

export default Attack;