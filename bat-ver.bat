@echo off
title Text-Based Batch Game

:START
cls
echo Welcome to the Text-Based Batch Game!
echo.
echo 1. Explore
echo 2. Check Inventory
echo 3. Quit
set /p choice="Enter your choice: "

if "%choice%"=="1" (
    call :Explore
) else if "%choice%"=="2" (
    call :CheckInventory
) else if "%choice%"=="3" (
    echo Thanks for playing!
    exit /b
) else (
    echo Invalid choice. Try again.
    timeout /t 2 /nobreak >nul
    goto :START
)

:Explore
cls
echo You are exploring the game world.
echo.
set /a "rand=%random% %% 2"
if %rand%==0 (
    echo You encounter an enemy!
    timeout /t 2 /nobreak >nul
    call :Fight
) else (
    echo You find an item!
    set /p "item=Enter the name of the item you found: "
    echo You found a %item% and added it to your inventory.
    set /p "continue=Press Enter to continue..."
    goto :START
)

:CheckInventory
cls
echo Your inventory is currently empty.
set /p "continue=Press Enter to continue..."
goto :START

:Fight
cls
echo You are in a battle!
echo.
echo 1. Attack
echo 2. Run
set /p choice="Enter your choice: "

if "%choice%"=="1" (
    set /a "damage=%random% %% 21"
    echo You attack the enemy for %damage% damage!
    timeout /t 2 /nobreak >nul
    echo The enemy attacks you!
    set /a "damage=%random% %% 16"
    echo The enemy hits you for %damage% damage!
    timeout /t 2 /nobreak >nul
    echo You have been defeated. Game Over.
    set /p "continue=Press Enter to continue..."
    goto :START
) else if "%choice%"=="2" (
    echo You run away from the enemy!
    timeout /t 2 /nobreak >nul
    goto :START
) else (
    echo Invalid choice. Try again.
    timeout /t 2 /nobreak >nul
    goto :Fight
)

