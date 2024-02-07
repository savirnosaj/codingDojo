int main()
{
    /* variables */
    float PI = 3.14159;
    /* aportes/inputs */
    int H;
    int R;
    /* totales */
    int P_base;
    int A_base;
    int area_Lateral;
    int area_Total;
    int volumen;
    
    /* comando para imprimir en la pantalla; similar a 'Escribir' en Pseint */
    cout << "Ingrese el valor de la altura:" << endl;
    /* comando para ingresar un argumento; similar a 'leer' en Pseint */
    cin >> H;
    
    cout << "Ingrese el radio:" << endl;
    cin >> R;
    
    /* performing calculations */
    P_base = 2 * PI * R;
    A_base = PI * (R * R);
    area_Lateral = 2 * PI * R * H;
    area_Total = area_Lateral + A_base;
    volumen = A_base * H;
    
    /* imprimiendo valores */
    cout << "CALCULOS PARCIALES" << endl;
    cout << "El Perimetro de la base es " << P_base << "cm" << endl;
    cout << "El Area de la base es " << A_base << "cm" << endl;
    
    cout << "DATOS DE RESULTADO" << endl;
    cout << "El area lateral del cilindro es de " << area_Lateral << "cm" << endl;

    return 0;
}

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    float area_lateral;
    float volumen;
    float area_total;
    float p_base;
    float A_base;
    float G;
    int H, R;
    float PI = 3.14;
    
    cout << "ingrese el valor de altura: " << endl;
    cin >> H;
    cout << "ingrese el valor del radio: " << endl;
    cin >> R;
    // calculos parciales
    p_base = 2 * PI * R;
    A_base = PI * pow(R,2);
    G = sqrt(pow(H,2) + pow(R,2));
    area_lateral = p_base * G / 2;
    area_total =  area_lateral * PI * pow(R,2);
    volumen = A_base * H / 3;
    
    // resultados en pantalla
    cout << "CALCULOS PARCIALES" << endl;
    cout << "El Perimetro de la base es " << p_base << " cm" << endl;
    cout << "El Area de la base es " << A_base << " cm" << endl;
    cout << "La valor de Generatriz es " << G << endl;
    cout << "DATOS DE RESULTADOS" << endl;
    cout << "El Area Lateral del cono es de " << area_lateral << " cm" << endl;
    cout << "El Area Total es de " << area_total << " cm2" << endl;
    cout << "El Volumen del cono es de " << volumen << " cm3" << endl;

    return 0;
}

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    float PI = 3.14;
    int radio_Casquete;
    int H_Casquete;
    float radio_De_Esfera;
    float area_Casquete;
    float volumen_Casquete;
    string opc;
    
    /*  */
    cout << "MENU\t" << endl;
    cout << "casquete esferico (escriba ce)" << endl;
    cout << "zona esferica (escriba ze)" << endl;
    cout << "salir" << endl;
    
    cin >> opc;
    
    if (opc == "ce") {
        cout << "Ingrese el radio del Casquete" << endl;
        cin >> radio_Casquete;
        cout << "Ingrese la altura del Casquete" << endl;
        cin >> H_Casquete;
        
        radio_De_Esfera = (pow(radio_Casquete, 2) + pow(H_Casquete, 2)) / (2 * H_Casquete);
        area_Casquete = 2 * PI * radio_De_Esfera * H_Casquete;
        volumen_Casquete = (PI * (pow(H_Casquete,2) / 3) * ((3 * radio_De_Esfera) - H_Casquete));
        
        cout << "DATOS DE ENTRADA DEL USUARIO" << endl;
        cout << "El radio del casquete es " << radio_Casquete << endl;
        cout << "La altura del casquete es " << H_Casquete << endl;
        
        cout << "RESULTADOS PASCIALES" << endl;
        cout << "El radio de la esfera es  " << radio_De_Esfera << endl;
        
        cout << "DATOS RESULTADOS" << endl;
        cout << "El area del casquete es de " << area_Casquete << endl;
        cout << "El volumen del casquete es de " << volumen_Casquete << endl;
    }
    else if (opc == "ze") {
    }
    else {
        cout << "Terminar session" << endl;
        return 0;
    }
    
    return 0;
}
