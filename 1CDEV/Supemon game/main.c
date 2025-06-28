#include <stdio.h>
#include <stdlib.h>

int main() {

    programLaunch();

    int choice;

    do {

        choice = displayMenu();

        switch(choice) {

            case 1:

                battle();

                break;

            case 2:

                shop();

                break;

            case 3:

                supemonCenter();

                break;

            case 4:

                printf("Goodbye!\n");

                break;

            default:

                printf("Feature not implemented yet!\n");

        }

    } while(choice != 4);

    return 0;

}
