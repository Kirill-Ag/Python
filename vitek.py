int main()
{
    setlocale (0,"");
    srand(time(NULL));

    int naperstok = rand()%3+1

    cout << "Перед вами три наперстка, два из которых пустые. Какой наперсток проверить?\n"
    
    int choise;
    cin >> choise;

    if (choise == naperstok)
       cout << "Угадали\n";
    else
       cout << "Не угадали!\n";

    system ("pause");
    return 0;
}   