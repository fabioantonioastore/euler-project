#include <stdio.h>


long double total_positions = 0;
const int GRID[2] = {20, 20};


void get_routers(int position[]){
    if (
        position[0] == GRID[0] &&
        position[1] == GRID[1]
    ){
        ++total_positions;
        return;
    }
    if (position[0] < GRID[0]){
        ++position[0];
        get_routers(position);
        --position[0];
    }
    if (position[1] < GRID[1]){
        ++position[1];
        get_routers(position);
        --position[1];
    }
}


int main(void){
    int position[2] = {0, 0};

    get_routers(position);

    printf("%Lf\n", total_positions);

    return 0;
}