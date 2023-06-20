let f = [100.2, 200.0, 300.3, 400.0, 500.0, 599.1, 650.1, 700.2, 800.0, 900.0, 1000.0, 1099.0, 1201.0, 1301.0];
let time_div = [2.5e-3, 1e-3, 500e-6, 500e-6, 250e-6, 250e-6, 250e-6, 250e-6, 250e-6, 250e-6, 250e-6, 250e-6, 100e-6, 100e-6];
let Vef_Vr = [454e-3, 919e-3, 1.39, 1.82, 2.02, 2.32, 2.42, 2.46, 2.24, 2.01, 1.92, 1.81, 1.53, 1.42];
let volt_div_Vr = [500e-3, 1000e-3, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1];
let volt_div_V0 = [5, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2]

let arredonda = 2, n = 6, L = 37.5e-3, C = 1.64e-6, R = 121.0, r = 11.5;

function omega(array) {
    let index = 0, w_vetor = [];
    while (index < f.length) {
        let w = 2 * Math.PI * array[index];
        w_vetor.push(w.toFixed(arredonda));
        index++;
    }
    return w_vetor;
}

function X_L(array1, array2) {
    let index = 0;
    let del_L = L * 0.05 + 1e-4;

    while (index < array1.length) {
        let reaIndutiva = array1[index] * L;

        let del_indutiva = Math.sqrt((L * array2[index]) ** 2 + (array1[index] * del_L) ** 2);

        console.log("X_L[" + (index + 1) + "] = " + reaIndutiva.toFixed(arredonda) + " ± " + del_indutiva.toFixed(arredonda));
        index++;
    }
}

function X_C(array1, array2) {
    let index = 0;
    let del_C = C * 0.019 + 2 * 0.01e-6;

    while (index < array1.length) {
        let reaCapacitiva = 1 / (array1[index] * C);

        let del_capacitiva = reaCapacitiva * Math.sqrt((array2[index] / array1[index]) ** 2 + (del_C / C) ** 2);

        console.log("X_C[" + (index + 1) + "] = " + reaCapacitiva.toFixed(arredonda) + " ± " + del_capacitiva.toFixed(arredonda));
        index++;
    }
}

function Z(array1, array2) {
    let index = 0;
    //Vetor das incertezas de cada impedância Z
    let del_Z = [30.9461785861966, 14.8263712370738, 9.58085493943158, 6.82644328471930, 4.48192534217070, 1.91401081028953, 1.35176491661760, 2.29858725922068, 4.94989942771673, 7.28825038281259, 9.27931506380116, 11.0211132667342, 12.6645599505143, 14.1799526875909]
    let A = (R + r) ** 2;

    while (index < array1.length) {
        let D = (L * array1[index] - 1 / (C * array1[index])) ** 2;
        let impedancia = Math.sqrt(A + D);
        let del_imp = del_Z[index];

        console.log("Z[" + (index + 1) + "] = " + impedancia.toFixed(arredonda) + " ± " + del_imp.toFixed(arredonda));
        index++;
    }
}

function Ief(array1, array2) {
    let index = 0;
    let del_R = 0.009 * R + 0.2;

    while (index < array1.length) {
        let corrente_eficaz = (array1[index] / R) * 10 ** (3);

        let del_corrente = (1 / R) * Math.sqrt((array2[index]) ** 2 + (corrente_eficaz * del_R) ** 2);

        console.log("Ief[" + (index + 1) + "] = " + corrente_eficaz.toFixed(arredonda) + " ± " + del_corrente.toFixed(arredonda));
        index++;
    }
}

function Δfrequencia(array1, array2, comando) {
    let index = 0;

    if (comando == 1) {
        while (index < array1.length) {
            let del_f = 0.2 * (array1[index] ** 2) * array2[index] / Math.sqrt(3);

            console.log("Δf[" + (index + 1) + "] = " + del_f.toFixed(arredonda));
            index++;
        }
    }

    if (comando >= 3) {
        let Δf = []
        while (index < array1.length) {
            let del_f = 0.2 * (array1[index] ** 2) * array2[index] / Math.sqrt(3);

            Δf.push(del_f.toFixed(arredonda));
            index++;
        }
        return Δf;
    }
}

function ΔporEscala(array, comando) {
    let index = 0;

    if (comando == 2 || comando == 6) {
        while (index < array.length) {
            let deltaEscala = (0.2 * array[index]) / Math.sqrt(3);

            console.log("ΔVef[" + (index + 1) + "] = " + deltaEscala.toFixed(arredonda));

            index++;
        }
    }

    if (comando == 7) {
        let delVef = [];

        while (index < array.length) {
            let deltaEscala = (0.2 * array[index]) / Math.sqrt(3);

            delVef.push(deltaEscala.toFixed(arredonda));
            index++;
        }
        return delVef;
    }
}

switch (n) {
    case 1:
        console.log("Incertezas de f: ");
        Δfrequencia(f, time_div, n);
        break;
    case 2:
        console.log("Incertezas de Vef/Vr: \n");
        ΔporEscala(volt_div_Vr, n);
        break;
    case 3:
        console.log("Reatância indutiva: \n");
        X_L(omega(f), omega(Δfrequencia(f, time_div, n)));
        break;
    case 4:
        console.log("Reatância capacitiva: \n");
        X_C(omega(f), omega(Δfrequencia(f, time_div, n)));
        break;
    case 5:
        console.log("Impedância total: \n");
        Z(omega(f), omega(Δfrequencia(f, time_div, n)));
        break;
    case 6:
        console.log("Incertezas de V0: \n");
        ΔporEscala(volt_div_V0, n);
        break;
    case 7:
        console.log("Corrente eficaz: \n");
        Ief(Vef_Vr, ΔporEscala(volt_div_Vr, n));
        break;
    default:
        break;
}