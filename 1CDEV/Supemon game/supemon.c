#include <stdio.h>

#include <stdlib.h>

#include <string.h>

#include <stdbool.h>



#define MAX_SUPEMONS 6

typedef struct {

    char name[20];

    int currentlvl;

    int currentHp;

    int maxHp;

    int experience;

    int currentAttack;

    int maxAttack;

    int currentDefense;

    int maxDefense;

    int currentEvasion;

    int maxEvasion;

    int currentAccuracy;

    int maxAccuracy;

    int speed;

} Supemon;

typedef struct {

    char name[30];

    int currentlvl;

    int currentHp;

    int maxHp;

    int experience;

    int currentAttack;

    int maxAttack;

    int currentDefense;

    int maxDefense;

    int currentEvasion;

    int maxEvasion;

    int currentAccuracy;

    int maxAccuracy;

    int speed;

} WildSupemon;

typedef struct {

    char itemName[30];

    int price;

    char gain[30];

}Item;

Item shopItems[]={

{"Potion",100, "+5HP"},

{"Super potion",300, "+10HP"},

{"Rare candy",700, "+1lvl"},

};

int shopItemCount = sizeof(shopItems) / sizeof(shopItems[0]);

typedef struct{

    int supcoins;

}Wallet;

typedef struct {

    char name[20];

    Supemon supemons[MAX_SUPEMONS];

    Supemon selectedSupemon;

    int supemonCount;

    Wallet wallet;

    Item items[10];

    int item_count;


} Player;

//declaration du joueur

Player player={

    .wallet.supcoins=500,

    .item_count=0,

};


void initSupemon(Supemon *s, const char *name, int hp, int atk, int def, int eva, int acc, int speed) {

    strcpy(s->name, name);

    s->currentlvl = 1;

    s->currentHp = s->maxHp = hp;

    s->currentAttack = s->maxAttack = atk;

    s->currentDefense = s->maxDefense = def;

    s->currentEvasion = s->maxEvasion = eva;

    s->currentAccuracy = s->maxAccuracy = acc;

    s->speed = speed;

    s->experience = 0;

}

// Fonction pour augmenter les statistiques d'un Supémon

void augmenterStatistiques(Supemon* supemon) {

    // Augmenter les statistiques de 30% à chaque niveau

    supemon->currentAttack = (int)(supemon->currentAttack * 1.3);

    supemon->currentDefense = (int)(supemon->currentDefense * 1.3);

    supemon->speed = (int)(supemon->speed * 1.3);

    supemon->currentHp = (int)(supemon->currentHp * 1.3);

    // Arrondir les valeurs des statistiques

    if ((supemon->currentAttack * 1.3) - (int)(supemon->currentAttack * 1.3) >= 0.5) {

        supemon->currentAttack++;

    }

    if ((supemon->currentDefense * 1.3) - (int)(supemon->currentDefense * 1.3) >= 0.5) {

        supemon->currentDefense++;

    }

    if ((supemon->speed * 1.3) - (int)(supemon->speed * 1.3) >= 0.5) {

        supemon->speed++;

    }

    if ((supemon->currentHp * 1.3) - (int)(supemon->currentHp * 1.3) >= 0.5) {

        supemon->currentHp++;

    }

}

// Fonction pour calculer l'expérience nécessaire pour atteindre un niveau

int experiencePourNiveau(int niveau) {

    return 500 + 1000 * (niveau - 1);  // Expérience nécessaire pour atteindre un nouveau niveau

}

// Fonction pour gérer l'expérience et augmenter de niveau

void gagnerNiveau(Supemon* supemon, int pointsExperience) {

    supemon->experience += pointsExperience;  // Ajouter l'expérience gagnée

    // Tant que le Supémon a assez d'expérience pour monter au niveau supérieur

    while (supemon->experience >= experiencePourNiveau(supemon->currentlvl + 1)) {

        supemon->experience -= experiencePourNiveau(supemon->currentlvl + 1);  // Retirer l'expérience nécessaire pour le prochain niveau

        supemon->currentlvl++;  // Incrémenter le niveau

        augmenterStatistiques(supemon);  // Augmenter les statistiques

    }

}

void programLaunch() {

    printf("Enter your name: ");

    scanf("%s", player.name);

    printf("Hello %s! \nWelcome to Supémon World!\n", player.name);

    // Initialisation des Supemons

    initSupemon(&player.supemons[0], "Supmander", 10, 1, 1, 1, 2, 1);

    initSupemon(&player.supemons[1], "Supasaur", 9, 1, 1, 3, 2, 2);

    initSupemon(&player.supemons[2], "Supirtle", 11, 1, 2, 2, 1, 2);

    printf("+-------------------------------+\n");

    printf("|   Choose your starter Supemon:|\n");

    printf("|   1-Supmander                 |\n");

    printf("|   2-Supasaur                  |\n");

    printf("|   3-Supirtle                  |\n");

    printf("+-------------------------------+\n");

    int choice;

    do {

        printf("Choice (1-3): ");

        scanf("%d", &choice);

    } while(choice < 1 || choice > 3);

    player.selectedSupemon = player.supemons[choice - 1];

    printf("\nYou have chosen %s!\n", player.selectedSupemon.name);

    printf("Stats - HP: %d ATK: %d DEF: %d\n\n",

           player.selectedSupemon.maxHp,

           player.selectedSupemon.maxAttack,

           player.selectedSupemon.maxDefense);

}

int displayMenu() {

    int choice;

    printf("\n+---------------------------------+\n");

    printf("| Where do you want to go?        |\n");

    printf("| 1. Into the Wild                |\n");

    printf("| 2. Shop                         |\n");

    printf("| 3. Supémon Center               |\n");

    printf("| 4. Quit                         |\n");

    printf("+---------------------------------+\n");

    printf("Choice (1-4): ");

    scanf("%d", &choice);

    return choice;

}

void displayBattleStats(WildSupemon wild) {

    printf("\n%s (enemy)\n", wild.name);

    printf("-------------------------------\n");

    printf("HP: %d          Lvl: %d\n", wild.currentHp, wild.currentlvl);

    printf("Atk: %d         Def: %d\n", wild.currentAttack, wild.currentDefense);

    printf("Acc: %d         Eva: %d\n", wild.currentAccuracy, wild.currentEvasion);

    printf("-------------------------------\n");

    printf("%s (%s)\n", player.selectedSupemon.name, player.name);

    printf("HP: %d          Lvl: %d\n", player.selectedSupemon.currentHp, player.selectedSupemon.currentlvl);

    printf("Atk: %d         Def: %d\n", player.selectedSupemon.currentAttack, player.selectedSupemon.currentDefense);

    printf("Acc: %d         Eva: %d\n", player.selectedSupemon.currentAccuracy, player.selectedSupemon.currentEvasion);

    printf("-------------------------------\n");

}

bool attemptEscape(Player *player, WildSupemon *wild) {

    float chance = (float)player->selectedSupemon.speed /

                 (player->selectedSupemon.speed + wild->speed);

    bool success = (float)rand()/RAND_MAX < chance;

    printf(success ? "Successful escape!\n" : "Leak fails!\n");

    return success;

}


void battle() {

    srand(time(NULL));

    WildSupemon wild;

    strcpy(wild.name, "Supmander");

    wild.currentHp = wild.maxHp = 10;

    wild.currentAttack = wild.maxAttack = 1;

    wild.currentDefense = wild.maxDefense = 1;

    wild.currentEvasion = wild.maxEvasion = 1;

    wild.currentAccuracy = wild.maxAccuracy = 2;

    wild.speed = 1;

    wild.currentlvl = 1;

    // Affichage du message d'apparition du Supémon sauvage au début du combat

    printf("\nA wild %s (Lvl %d) appeared!\n", wild.name, wild.currentlvl);

    int battleEnded = 0;  // Variable pour indiquer si le combat est terminé

    // Boucle de combat

    while(player.selectedSupemon.currentHp > 0 && wild.currentHp > 0) {

        displayBattleStats(wild);

        int action;

        printf("+-------------------------------+\n");

        printf("|What will you do?              |\n");

        printf("| 1-Move                        |\n");

        printf("| 2-Change Supemon              |\n");

        printf("| 3-Use item                    |\n");

        printf("| 4-Capture                     |\n");

        printf("| 5-Run away                    |\n");

        printf("+-------------------------------+\n");

        printf("Choice: ");

        scanf("%d", &action);

        // Traitement de l'action du joueur

        if(action == 1) {

            // Sélection et traitement des moves

            printf("+-------------------------------+\n");

            printf("|Choose a move:                 |\n");

            if(strcmp(player.selectedSupemon.name, "Supmander") == 0) {

                printf("|1-Scratch (3 DMG)             |\n");

                printf("|2-Grawl (+1 ATK)              |\n");

            }

            else if(strcmp(player.selectedSupemon.name, "Supasaur") == 0) {

                printf("|1-Pound (2 DMG)               |\n");

                printf("|2-Foliage (+1 EVA)            |\n");

            }

            else {

                printf("|1-Pound (2 DMG)               |\n");

                printf("|2-Shell (+1 DEF)              |\n");

            }

            printf("|3-Cancel                       |\n");

            printf("+-------------------------------+\n");

            int move;

            printf("Move choice: ");

            scanf("%d", &move);

            if(move == 1) {

                // Effectuer l'attaque du joueur

                int baseDmg = (strcmp(player.selectedSupemon.name, "Supmander") == 0) ? 3 : 2;

                // Calcul précision

                float hitRate = (float)player.selectedSupemon.currentAccuracy /

                              (player.selectedSupemon.currentAccuracy + wild.currentEvasion) + 0.1f;

                hitRate = fminf(hitRate, 1.0f);

                if((float)rand()/RAND_MAX < hitRate) {

                    // Calcul des dégâts

                    float rawDmg = (player.selectedSupemon.currentAttack * baseDmg) / (float)wild.currentDefense;

                    int finalDmg = (int)rawDmg;

                    // Arrondi aléatoire si nécessaire

                    if(rawDmg - finalDmg > 0) {

                        finalDmg += (rand() % 2); // 50% chance d'arrondir à l'inférieur ou supérieur

                    }

                    printf("%s dealt %d damage!\n", player.selectedSupemon.name, finalDmg);

                    wild.currentHp -= finalDmg;

                } else {

                    printf("%s's attack missed!\n", player.selectedSupemon.name);

                }

            }

            else if(move == 2) { // Buff

                if(strcmp(player.selectedSupemon.name, "Supmander") == 0) {

                    player.selectedSupemon.currentAttack++;

                    printf("Attack increased!\n");

                }

                else if(strcmp(player.selectedSupemon.name, "Supasaur") == 0) {

                    player.selectedSupemon.currentEvasion++;

                    printf("Evasion increased!\n");

                }

                else {

                    player.selectedSupemon.currentDefense++;

                    printf("Defense increased!\n");

                }

            }

        }

        else if(action == 2){

            changeSupemon();

        }

        else if(action == 3){

            useItem();

        }

        else if(action == 4) {
            // Logique de capture
            float captureChance = ((wild.maxHp - wild.currentHp)/(float)wild.maxHp) - 0.5f;
            captureChance = fmaxf(captureChance, 0.0f);  // Assurer que la chance ne soit jamais négative

            printf("Capture attempt... (%.0f%% chance)\n", captureChance * 100);

            if((float)rand() / RAND_MAX < captureChance) {
                printf("Success! %s captured!\n", wild.name);

                // Ajouter le Supémon capturé à l'inventaire du joueur
                if (player.supemonCount < MAX_SUPEMONS) {
                    // Ajouter le Supémon à l'inventaire
                    Supemon capturedSupemon;
                    strcpy(capturedSupemon.name, wild.name);
                    capturedSupemon.currentlvl = wild.currentlvl;
                    capturedSupemon.currentHp = wild.currentHp;
                    capturedSupemon.maxHp = wild.maxHp;
                    capturedSupemon.currentAttack = wild.currentAttack;
                    capturedSupemon.maxAttack = wild.maxAttack;
                    capturedSupemon.currentDefense = wild.currentDefense;
                    capturedSupemon.maxDefense = wild.maxDefense;
                    capturedSupemon.currentEvasion = wild.currentEvasion;
                    capturedSupemon.maxEvasion = wild.maxEvasion;
                    capturedSupemon.currentAccuracy = wild.currentAccuracy;
                    capturedSupemon.maxAccuracy = wild.maxAccuracy;
                    capturedSupemon.speed = wild.speed;

                    // Ajouter à l'inventaire
                    player.supemons[player.supemonCount] = capturedSupemon;
                    player.supemonCount++;  // Augmenter le nombre de Supémons dans l'inventaire
                } else {
                    printf("Your inventory is full! You cannot capture %s.\n", wild.name);
                }

                battleEnded = 1;  // Fin du combat
            } else {
                printf("Capture failed!\n");
            }
        }

        else if(action == 5) {

            // Logique de fuite

            float fleeChance = (float)player.selectedSupemon.speed /

                             (player.selectedSupemon.speed + wild.speed);

            printf("Attempting to flee... (%.0f%% chance)\n", fleeChance*100);

            if((float)rand()/RAND_MAX < fleeChance) {

                printf("Got away safely!\n");

                return;

            } else {

                printf("Couldn't escape!\n");

            }

        }

        // Vérification de la fin du combat

        if (wild.currentHp <= 0 || battleEnded) {

            printf("%s fainted!\n", wild.name);

            if (player.selectedSupemon.currentHp > 0) {

                // Récompenses si le joueur gagne

                int supcoins = 100 + rand() % 401;  // 100 à 500 Supcoins

                printf("You won the battle! You earned %d Supcoins!\n", supcoins);

                // Récompense d'expérience

                int expGain = (100 + rand() % 401) * wild.currentlvl;  // 100 à 500 fois le niveau de l'ennemi

                printf("%s gained %d experience points!\n", player.selectedSupemon.name, expGain);

                // Augmenter l'expérience du Supémon du joueur

                int pointsExperience = rand() % 401 + 100;  // Entre 100 et 500 (comme spécifié dans la description)

                gagnerNiveau(&player.selectedSupemon, pointsExperience);

            }

            return;

        }

        // Tour de l'ennemi si toujours en combat

        if(wild.currentHp > 0) {

            // Calcul attaque ennemie avec formule

            float hitRate = (float)wild.currentAccuracy /

                          (wild.currentAccuracy + player.selectedSupemon.currentEvasion) + 0.1f;

            hitRate = fminf(hitRate, 1.0f);

            if((float)rand()/RAND_MAX < hitRate) {

                int baseDmg = 2; // Valeur de base de l'attaque ennemie

                float rawDmg = (wild.currentAttack * baseDmg) / (float)player.selectedSupemon.currentDefense;

                int finalDmg = (int)rawDmg;

                if(rawDmg - finalDmg > 0) {

                    finalDmg += (rand() % 2);

                }

                player.selectedSupemon.currentHp -= finalDmg;

                printf("%s dealt %d damage!\n", wild.name, finalDmg);

            } else {

                printf("%s's attack missed!\n", wild.name);

            }

        }

    }

}

void changeSupemon() {
    printf("\n+-------------------------------+\n");
    printf("|    Choose a Supemon:         |\n");
    for (int i = 0; i < 3; i++) {
        printf("|  %d-%s (HP: %d/%d)        |\n", i + 1, player.supemons[i].name, player.supemons[i].currentHp, player.supemons[i].maxHp);
    }
    printf("+-------------------------------+\n");

    int choice;
    do {
        printf("Choice (1-3): ");
        scanf("%d", &choice);
    } while (choice < 1 || choice > 3 || player.supemons[choice - 1].currentHp <= 0);

    player.selectedSupemon = player.supemons[choice - 1];
    printf("\nYou have switched to %s!\n", player.selectedSupemon.name);
    printf("Stats - HP: %d ATK: %d DEF: %d\n\n",
           player.selectedSupemon.currentHp,
           player.selectedSupemon.currentAttack,
           player.selectedSupemon.currentDefense);
}

void useItem() {
    if (player.item_count == 0) {
        printf("\nYou have no items to use!\n");
        return;
    }

    printf("\n+-------------------------------+\n");
    printf("|    Choose an item to use:     |\n");
    for (int i = 0; i < player.item_count; i++) {
        printf("|  %d-%s |\n", i + 1, player.items[i].itemName);
    }
    printf("+-------------------------------+\n");

    int choice;
    printf("Choice (1-%d): ", player.item_count);
    scanf("%d", &choice);

    if (choice < 1 || choice > player.item_count) {
        printf("Invalid choice.\n");
        return;
    }

    printf("\nYou used %s!\n", player.items[choice - 1].itemName);
    player.item_count--;
}


void shop(){

    int shopChoice;

    do{

        printf("\nWelcome to Supemon Shop!\n");

        printf("----------------------------------\n");

        printf("Wallet: %dSupC           Items: %d\n", player.wallet.supcoins, player.item_count);

        printf("%s lvl: %d         HP: %d\n",player.selectedSupemon.name, player.selectedSupemon.currentlvl,player.selectedSupemon.currentHp);

        printf("----------------------------------\n");

        printf("\n+------------------------------+\n");

        printf("| What do you want to do:  |\n");

        printf("|  1-Buy                   |\n");

        printf("|  2-Sell                  |\n");

        printf("|  3-Leave the shop        |\n");

        printf("+--------------------------+\n");

        printf("Choice (1-3): ");

        scanf("%d", &shopChoice);

        switch (shopChoice){

            case 1:

                buyItemsMenu();

                break;

            case 2:

                sellItemsMenu();

                break;

            case 3:

                displayMenu();


            default:

                printf("Invalid choice.Please make another choice.\n");

        }

    }while(shopChoice !=3);

}

void buyItemsMenu(){

    displayItemList(shopItems, shopItemCount);

    printf("Choose an item to buy (1-%d) or enter 0 to go back: ", shopItemCount);

    int buyChoice;

    scanf("%d", &buyChoice);

    if (buyChoice >= 1 && buyChoice <= shopItemCount) {

        buyItem(shopItems, buyChoice - 1);

    } else if (buyChoice == 0) {

        printf("Going back to the shop menu.\n");

    } else {

        printf("Invalid choice. Please try again.\n");

    }

}

void displayItemList(Item items[], int itemCount) {

    printf("+----------------------------------+\n");

    printf("| Choose your item:                |\n");

    printf("|  0-Go back                       |\n");

    for (int i = 0; i < itemCount; i++) {

        printf("|  %d-%s(%s)    %dSupC            |\n",i + 1, items[i].itemName, items[i].gain,items[i].price);

    }

    printf("+----------------------------------+\n");

}

void buyItem(Item items[], int itemIndex) {

    if (player.item_count < sizeof(player.items) / sizeof(player.items[0])) {

        if (player.wallet.supcoins >= items[itemIndex].price) {

            player.wallet.supcoins -= items[itemIndex].price;

            strcpy(player.items[player.item_count].itemName, items[itemIndex].itemName);

            player.items[player.item_count].price = items[itemIndex].price / 2;

            player.item_count++;

            printf("You bought %s for %d Supcoins.\n", items[itemIndex].itemName, items[itemIndex].price);

        } else {

            printf("Not enough Supcoins to buy %s. Choose another item or leave the shop.\n", items[itemIndex].itemName);

        }

    } else {

        printf("Your inventory is full. Sell or use some items before buying more.\n");

    }

}

void sellItemsMenu() {
    if (player.item_count == 0) {
        printf("You have no items to sell!\n");
        return;
    }

    sellItem(player.items, &player.item_count);
}


//ne fonctionne pas tres bien ca ne renvoie pas l'argent dans le wallet et ca crash

//je sais pk mais je narrive paq a regler le pb

void sellItem(Item playerItems[], int *playerItemCount) {
    if (*playerItemCount == 0) {
        printf("You have no items to sell!\n");
        return;
    }

    displayItemList(playerItems, *playerItemCount);

    printf("Choose an item to sell (1-%d) or enter 0 to go back: ", *playerItemCount);
    int sellChoice;
    scanf("%d", &sellChoice);

    if (sellChoice < 1 || sellChoice > *playerItemCount) {
        printf("Invalid choice. Going back.\n");
        return;
    }

    // Récupérer le prix de l’objet vendu
    int itemPrice = playerItems[sellChoice - 1].price;
    player.wallet.supcoins += itemPrice;

    printf("You sold %s for %d Supcoins.\n", playerItems[sellChoice - 1].itemName, itemPrice);

    // Décaler les objets restants
    for (int i = sellChoice - 1; i < *playerItemCount - 1; i++) {
        playerItems[i] = playerItems[i + 1];
    }

    // Réduire le nombre total d'objets
    (*playerItemCount)--;

    printf("Wallet balance: %d Supcoins.\n", player.wallet.supcoins);
}


void supemonCenter(){

    printf("\nWelcome to the Supemon Center!\n");

    printf("-------------------------------\n");

    printf("\nBefore Healing:\n");

    for (int i = 0; i < player.item_count; i++) {

        printf("Supemon %d: %s | Health: %d | HP Lost: %d\n", i+1, player.supemons[i].name, player.supemons[i].currentHp, player.supemons[i].maxHp);

    }

    printf("\nHealing Supemons...\n");

    for (int i = 0; i < player.item_count; i++) {

        int beforeHealingHP = player.supemons[i].currentHp;

        player.supemons[i].currentHp += player.supemons[i].maxHp;

        player.supemons[i].maxHp = 0;

        int afterHealingHP = player.supemons[i].currentHp;

        int healedHP = afterHealingHP - beforeHealingHP;

        printf("Supemon %d: %s | Health: %d | Healed: %d HP\n", i+1, player.supemons[i].name, player.supemons[i].currentHp, healedHP);

    }

}
