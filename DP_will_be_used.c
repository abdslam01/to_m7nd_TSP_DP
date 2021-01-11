#include<stdio.h>
#include<stdlib.h>
//#include"instances2.h"
// dist[49][49] nmbr_cities
int nmbr_cities=16;
int dist[16][16]={
{0,633,257,91,412,150,80,134,259,505,353,324,70,211,268,246},
{633,0,390,661,227,488,572,530,555,289,282,638,567,466,420,745},
{257,390,0,228,169,112,196,154,372,262,110,437,191,74,53,472},
{91,661,228,0,383,120,77,105,175,476,324,240,27,182,239,237},
{412,227,169,383,0,267,351,309,338,196,61,421,346,243,199,528},
{150,488,112,120,267,0,63,34,264,360,208,329,83,105,123,364},
{80,572,196,77,351,63,0,29,232,444,292,297,47,150,207,332},
{134,530,154,105,309,34,29,0,249,402,250,314,68,108,165,349},
{259,555,372,175,338,264,232,249,0,495,352,95,189,326,383,202},
{505,289,262,476,196,360,444,402,495,0,154,578,439,336,240,685},
{353,282,110,324,61,208,292,250,352,154,0,435,287,184,140,542},
{324,638,437,240,421,329,297,314,95,578,435,0,254,391,448,157},
{70,567,191,27,346,83,47,68,189,439,287,254,0,145,202,289},
{211,466,74,182,243,105,150,108,326,336,184,391,145,0,57,426},
{268,420,53,239,199,123,207,165,383,240,140,448,202,57,0,483},
{246,745,472,237,528,364,332,349,202,685,542,157,289,426,483,0}
};

//fonction auxilière
int is_in_table(int ele, int *T){
	int i,lenght=sizeof(*T)/sizeof(int);
	for(i=0; i<lenght; i++)
		if(T[i]==ele)
			return 1;
	return 0;
}
int min(int a, int b){
	return (a<b)?a:b;
}
int minTab(int *T){
	int i, lenght=sizeof(*T);
	if(lenght){
		int minimum=T[0];
		for(i=1; i<lenght; i++)
			if(T[i]<minimum)
				minimum=T[i];
		return minimum;
	}else{
		printf("minTab: pas de min, tableau est vide");
		exit(-2);
	}
}
void del_ele_table(int **T, int ele){
	int i,j,lenght=sizeof(**T);
	for(i=0; i<lenght; i++){
		if(ele==(*T)[i]){
			for(j=i; j<lenght-1; j++)
				(*T)[j]=(*T)[j+1];
			(*T)=(int*)realloc(*T, lenght-1);
		}
	}
}
int* createTable(int upBound, int exclu){
	int i,k,*T;
	T=(int*)malloc(upBound-1);
	for(i=k=0; i<upBound; i++)
		if(i!=exclu)
			T[k++]=i;
	return T;
}
void insertElementInFirst(int **T, int ele){
	int i,lenght=sizeof(**T)/sizeof(int);
	(*T)=(int*)realloc(*T, lenght+1);
	for(i=lenght; i>0; i--)
		(*T)[i]=(*T)[i-1];
	(*T)[0]=ele;
}
int* addInitialPointToPath(int *T, int init_point){
	insertElementInFirst(&T, init_point);
	int lenght=sizeof(*T)/sizeof(int);
	T=(int*)realloc(T, lenght+1);
	T[lenght]=init_point;
	return T;
}
//fonction principale
int *l_cout, *avant_dernier_ville;
int rec_tsp_solve(int vv_cible, int **vvilles_inter){
	if(is_in_table(vv_cible, *vvilles_inter)){
		printf("vv_cible not in vvilles_inter");
		exit(1);
	}
	if(sizeof(**vvilles_inter)){
		int i,lenght=sizeof(**vvilles_inter)/sizeof(int);
		int tmpTab[lenght];
		for(i=0; i<lenght; i++){
			del_ele_table(vvilles_inter, i);
			printf("%d ",__LINE__);
			tmpTab[i]=dist[i][vv_cible]+rec_tsp_solve(i,vvilles_inter);
			//tmpTab[i]=*(dist+i*nmbr_cities+vv_cible)+rec_tsp_solve(i,vvilles_inter);
			// dist[i][vv_cible]
			return minTab(tmpTab);
		}
	}else{
		*l_cout=dist[0][vv_cible];
		*avant_dernier_ville=vv_cible;
		return *l_cout;
	}
}

void tsp_rec_solve(int **cout, int nb_villes, int v_cible){
	int *meilleur_tour, taille_cout=nb_villes;
	int *villes_inter=createTable(taille_cout, v_cible);
	int i=0;
	int cout_optimal=-1;
	printf(" %d ",__LINE__);
	while(1){
		rec_tsp_solve(v_cible, &villes_inter);
		if(cout_optimal==-1) cout_optimal=*l_cout;
		if(*avant_dernier_ville == v_cible)
			break;
		insertElementInFirst(&meilleur_tour, *avant_dernier_ville);
		del_ele_table(&villes_inter, *avant_dernier_ville);
	}
	meilleur_tour=addInitialPointToPath(meilleur_tour, v_cible);
	int lenght=sizeof(*meilleur_tour)/sizeof(int);
	printf("le tour est: ");
	for(i=0;i<lenght;i++) printf("%d->",meilleur_tour[i]);
	printf("\nle cout est: %d", *l_cout);
}

// matrix[x][y] == matrix + x*Column + y
void main(){
//	int i, *T=createTable(5,1);
//	for(i=0;i<4;i++) printf("%d ",T[i]);
//	printf("\n");
//	del_ele_table(&T, 3);
//	for(i=0;i<4;i++) printf("%d ",T[i]);
//	free(T);
//	printf("\n");
//	for(i=0;i<4;i++) printf("%d ",T[i]);
	tsp_rec_solve((int**)dist, nmbr_cities, 0);
}
