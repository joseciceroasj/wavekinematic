function varargout = CINEMATICAONDA(varargin)
% CINEMATICAONDA MATLAB code for CINEMATICAONDA.fig
%      CINEMATICAONDA, by itself, creates a new CINEMATICAONDA or raises the existing
%      singleton*.
%
%      H = CINEMATICAONDA returns the handle to a new CINEMATICAONDA or the handle to
%      the existing singleton*.
%
%      CINEMATICAONDA('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in CINEMATICAONDA.M with the given input arguments.
%
%      CINEMATICAONDA('Property','Value',...) creates a new CINEMATICAONDA or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before CINEMATICAONDA_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to CINEMATICAONDA_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help CINEMATICAONDA

% Last Modified by GUIDE v2.5 13-Dec-2018 10:18:03

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @CINEMATICAONDA_OpeningFcn, ...
                   'gui_OutputFcn',  @CINEMATICAONDA_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before CINEMATICAONDA is made visible.
function CINEMATICAONDA_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to CINEMATICAONDA (see VARARGIN)

% Choose default command line output for CINEMATICAONDA
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes CINEMATICAONDA wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = CINEMATICAONDA_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function T_Callback(hObject, eventdata, handles)
% hObject    handle to T (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of T as text
%        str2double(get(hObject,'String')) returns contents of T as a double


% --- Executes during object creation, after setting all properties.
function T_CreateFcn(hObject, eventdata, handles)
% hObject    handle to T (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function d_Callback(hObject, eventdata, handles)
% hObject    handle to d (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of d as text
%        str2double(get(hObject,'String')) returns contents of d as a double


% --- Executes during object creation, after setting all properties.
function d_CreateFcn(hObject, eventdata, handles)
% hObject    handle to d (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function H_Callback(hObject, eventdata, handles)
% hObject    handle to H (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of H as text
%        str2double(get(hObject,'String')) returns contents of H as a double


% --- Executes during object creation, after setting all properties.
function H_CreateFcn(hObject, eventdata, handles)
% hObject    handle to H (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function cxL_CreateFcn(hObject, eventdata, handles)
% hObject    handle to cxL (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
format bank;

H = str2double(get(handles.H,'String'));
T = str2double(get(handles.T,'String'));
d = str2double(get(handles.d,'String'));
x = str2double(get(handles.x,'String'));
t = str2double(get(handles.tempo,'String'));
g =9.81;
W = (4*pi^2*d)/(g*(T^2));
f =1 + (0.666*W + 0.445*W -0.105*W + 0.272*W);
L = (T*sqrt(g*d)*sqrt(f/(1+W*f)));
k = (2*pi/L);
w = (2*pi/T);
c = w/k;

set(handles.cxL, 'String', sprintf('%.2f',L));
set(handles.text10, 'String', sprintf('%.2f',k));
set(handles.text11, 'String', sprintf('%.2f',c));
set(handles.text12, 'String', sprintf('%.2f',w));



%ARMAZENANDO OS VALORES - LEMBRAR QUE O NEGATIVO APARECE PARA SE ADEQUAR AO EIXO, CONFORME PLANILHA DO EXCEL.    
%Velocidade horizontal, superfície e d = L/2
uhL0 = (((9.81*k*H)/(2*w))*(cosh(k*(0+d))/cosh(k*d))*cos(k*(x-c*t)));
uhL2 =(((9.81*k*H)/(2*w))*(cosh(k*(-L/2+d))/cosh(k*d))*cos(k*(x-c*t)));
%Velocidade vertical, superfície e d = L/2
uvL0 =(((9.81*k*H)/(2*w))*(sinh(k*(0+d))/cosh(k*d))*sin(k*(x-c*t)));
uvL2 =(((9.81*k*H)/(2*w))*(sinh(k*(-L/2+d))/cosh(k*d))*sin(k*(x-c*t)));
%Aceleração vertical, superfície e d = L/2
AvL0 =-(((9.81*k*H)/(2))*(sinh(k*(0+d))/cosh(k*d))*cos(k*(x-c*t)));
AvL2 =-(((9.81*k*H)/(2))*(sinh(k*(-L/2+d))/cosh(k*d))*cos(k*(x-c*t)));
%Aceleração horizontal, superfície e d = L/2
AhL0 =(((9.81*k*H)/(2))*(cosh(k*(0+d))/cosh(k*d))*sin(k*(x-c*t)));
AhL2 =(((9.81*k*H)/(2))*(cosh(k*(-L/2+d))/cosh(k*d))*sin(k*(x-c*t)));

%CALCULO DO PERCENTUAL 
PVh = 100*(uhL2/uhL0);
PVv = 100*(uvL2/uvL0);
PAv = 100*(AvL2/AvL0);
PAh = 100*(AhL2/AhL0);

%MOSTRANDO O PERCENTUAL NAS CAIXAS
set(handles.text39, 'String', sprintf('%.2f',PVh));
set(handles.text40, 'String', sprintf('%.2f',PVv));
set(handles.text41, 'String', sprintf('%.2f',PAv));
set(handles.text42, 'String', sprintf('%.2f',PAh));

%PREVENDO AS DIVISÕES POR ZERO NA PORCENTAGEM
if (isnan(PVv))
    warndlg('Divisão por zero! Velocidade vertical nula em superfície e em L/2!','Erro');
    set(handles.text40, 'String', '-');
end
 if (isnan(PVh))
    warndlg('Divisão por zero! Velocidade horizontal nula em superfície e em L/2!','Erro');
    set(handles.text39, 'String', '-');
end
if (isnan(PAh))
    warndlg('Divisão por zero! Aceleração horizontal nula em superfície e em L/2!','Erro');
    set(handles.text41, 'String', '-');
end 
if isnan(PAv)
    warndlg('Divisão por zero! Aceleração vertical nula em superfície e em L/2!','Erro');
    set(handles.text42, 'String', '-');
end

    %MENSAGENS DE AVISO, CASO O COMP. DE ONDA ULTRAPASSE A PROFUNDIDADE
if (L/2>d)  
warndlg('Profundidade menor que a metade do comprimento de onda!','Atenção');
set(handles.text39, 'String', '-');
set(handles.text40, 'String', '-');
set(handles.text41, 'String', '-');
set(handles.text42, 'String', '-');
end

graficos(handles);


function x_Callback(hObject, eventdata, handles)
% hObject    handle to x (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of x as text
%        str2double(get(hObject,'String')) returns contents of x as a double


% --- Executes during object creation, after setting all properties.
function x_CreateFcn(hObject, eventdata, handles)
% hObject    handle to x (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function tempo_Callback(hObject, eventdata, handles)
% hObject    handle to tempo (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of tempo as text
%        str2double(get(hObject,'String')) returns contents of tempo as a double


% --- Executes during object creation, after setting all properties.
function tempo_CreateFcn(hObject, eventdata, handles)
% hObject    handle to tempo (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in radiobutton3.
function radiobutton3_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton3


% --- Executes on button press in radiobutton4.
function radiobutton4_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton4


% --- Executes on button press in radiobutton5.
function radiobutton5_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton5


% --- Executes on button press in radiobutton6.
function radiobutton6_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton6


% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

%Recebendo dados do usuário
H = str2double(get(handles.H,'String'));
T = str2double(get(handles.T,'String'));
d = str2double(get(handles.d,'String'));
x = str2double(get(handles.x,'String'));
t = str2double(get(handles.tempo,'String'));

%H=1; T=10; d=50; x=1; t=0;

%Cálculo de comprimento de onda
g =9.81;
W = (4*pi^2*d)/(g*(T^2));
f =1 + (0.666*W + 0.445*W -0.105*W + 0.272*W);
L = (T*sqrt(g*d)*sqrt(f/(1+W*f)));
k = (2*pi/L);
w = (2*pi/T);
c = w/k;

%Mostrando nas caixas
set(handles.cxL, 'String', num2str(L));
set(handles.text10, 'String', num2str(k));
set(handles.text11, 'String', num2str(c));
set(handles.text12, 'String', num2str(w));

z =0;

if (L/2>d)
    zd = d;
else
    zd = L/2;
end



% --- Executes on button press in VelVertical.
function VelVertical_Callback(hObject, eventdata, handles)
% hObject    handle to VelVertical (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
%Recebendo dados do usuário

graficos(handles);

% Hint: get(hObject,'Value') returns toggle state of VelVertical


% --- Executes on button press in VelHorizontal.
function VelHorizontal_Callback(hObject, eventdata, handles)
% hObject    handle to VelHorizontal (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

graficos(handles);




% --- Executes on button press in AcelVertical.
function AcelVertical_Callback(hObject, eventdata, handles)
% hObject    handle to AcelVertical (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

graficos(handles);


% --- Executes on button press in AcelHorizontal.
function AcelHorizontal_Callback(hObject, eventdata, handles)
% hObject    handle to AcelHorizontal (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

graficos(handles);

% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes during object creation, after setting all properties.
function axes1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to axes1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: place code in OpeningFcn to populate axes1


% --- Executes on button press in pushbutton4.
function pushbutton4_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
%helpdlg('Para plotar o gráfico, você deve selecionar uma ou mais opções de aceleração e velocidade! Além disso, selecione a profundidade máxima desejada! Esse programa irá calcular e plotar as velocidades e acelerações com a profundidade recebendo os dados de entrada do usuário.','Ajuda');


% --- Executes on button press in pushbutton5.
function pushbutton6_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in pushbutton6.
% hObject    handle to pushbutton6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

%Recebendo dados do usuário
H = str2double(get(handles.H,'String'));
T = str2double(get(handles.T,'String'));
d = str2double(get(handles.d,'String'));
x = str2double(get(handles.x,'String'));
t = str2double(get(handles.tempo,'String'));

%H=1; T=10; d=50; x=1; t=0;

%Cálculo de comprimento de onda
g =9.81;
W = (4*pi^2*d)/(g*(T^2));
f =1 + (0.666*W + 0.445*W -0.105*W + 0.272*W);
L = (T*sqrt(g*d)*sqrt(f/(1+W*f)));
k = (2*pi/L);
w = (2*pi/T);
c = w/k;
zd = d;

%Mostrando nas caixas
set(handles.cxL, 'String', num2str(L));
set(handles.text10, 'String', num2str(k));
set(handles.text11, 'String', num2str(c));
set(handles.text12, 'String', num2str(w));


%RADIO BUTTON
z =0;
RB1 = get(handles.radiobutton10,'Value');
RB2 = get(handles.radiobutton11,'Value');
RB3 = get(handles.radiobutton12,'Value');
if RB1 == 1 %até L/2
    if(L/2>d)
        zd = d;
        
    else
        zd = L/2;
    end 
end
if RB2 == 1
    if(L>d)
        zd = d;
        
    else
        zd = L;
    end 
end
if RB3 == 1
        zd = d;
end


for i= 1:zd
    %Calcula a velocidade horizontal 
    uh(i)=(((9.81*k*H)/(2*w))*(cosh(k*(z+zd))/cosh(k*zd))*cos(k*(x-c*t)));
    %Calcula a velocidade vertical
    uv(i)=(((9.81*k*H)/(2*w))*(sinh(k*(z+zd))/cosh(k*zd))*sin(k*(x-c*t)));
    %Calcula a aceleração vertical 
    Av(i)=(((9.81*k*H)/(2))*(sinh(k*(z+zd))/cosh(k*zd))*cos(k*(x-c*t)));
    %Calcula a aceleração horizontal
    Ah(i)=(((9.81*k*H)/(2))*(cosh(k*(z+zd))/cosh(k*zd))*sin(k*(x-c*t)));
    
    z = z - 1; 
    %Mostrando o vetor
    disp(i);
    %Mostrando as velocidades
    disp(uh(i));
    disp (uv(i));
    %Mostrando as acelerações
    disp(Av(i));
    disp(Ah(i));
    
    vetori(i)= i;
    vetori(i)= z;
    
end


%Obtendo dados do usuário - CheckBox e RadioButton
VVertical = get(handles.VelVertical,'Value');
VHorizontal = get(handles.VelHorizontal,'Value');
AVertical = get(handles.AcelVertical,'Value');
AHorizontal = get(handles.AcelHorizontal,'Value');


cla reset;
hold on

%axis (inf);
j = 1;
if VVertical == 1 
    plot1(j) = plot(uv,vetori,'Parent',handles.axes1);
    %plot(uv,vetori, 'DisplayName','VV')
    %legend ('Velocidade Vertical');
    set(plot1(j),'DisplayName','Velocidade Vertical');
    grid on
    j = j+1;
    hold on;
end
%hold on
if VHorizontal == 1
    plot1(j)= plot(uh,vetori,'Parent',handles.axes1);
%     plot(uh,vetori,'DisplayName','VH')
    %legend ('Velocidade Horizontal');
    set(plot1(j),'DisplayName','Velocidade Horizontal');
    grid on
    j=j+1;
    hold on;
end

if AVertical == 1
    plot1(j)= plot(Av,vetori,'Parent',handles.axes1);
    %legend ('Aceleração Vertical');
    set(plot1(j),'DisplayName','Aceleração Vertical');
    grid on
    j = j+1;
    hold on;
end
if AHorizontal == 1
    plot1(j)= plot(Ah,vetori, 'Parent',handles.axes1);
   % legend ('Aceleração Horizontal');
    set(plot1(j),'DisplayName','Aceleração Vertical');
    grid on
    j = j+1;
    hold on;
end
legend1 = legend(handles.axes1,'show');

% pegar = get(handles.uibuttongroup4,'SelectObject')



% --- Executes on key press with focus on pushbutton6 and none of its controls.
function pushbutton6_KeyPressFcn(hObject, eventdata, handles)
% hObject    handle to pushbutton6 (see GCBO)
% eventdata  structure with the following fields (see MATLAB.UI.CONTROL.UICONTROL)
%	Key: name of the key that was pressed, in lower case
%	Character: character interpretation of the key(s) that was pressed
%	Modifier: name(s) of the modifier key(s) (i.e., control, shift) pressed
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in VelVertical.
function checkbox5_Callback(hObject, eventdata, handles)
% hObject    handle to VelVertical (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of VelVertical


% --- Executes on button press in VelHorizontal.
function checkbox6_Callback(hObject, eventdata, handles)
% hObject    handle to VelHorizontal (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of VelHorizontal


% --- Executes on button press in AcelVertical.
function checkbox7_Callback(hObject, eventdata, handles)
% hObject    handle to AcelVertical (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of AcelVertical


% --- Executes on button press in AcelHorizontal.
function checkbox8_Callback(hObject, eventdata, handles)
% hObject    handle to AcelHorizontal (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of AcelHorizontal


% --- Executes during object creation, after setting all properties.
function uibuttongroup4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to uibuttongroup4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called


% --- Executes when selected object is changed in uibuttongroup4.
function uibuttongroup4_SelectionChangedFcn(hObject, eventdata, handles)
% hObject    handle to the selected object in uibuttongroup4 
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in pushbutton7.
function pushbutton7_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton7 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in radiobutton10.
function radiobutton10_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton10 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

graficos(handles);

% --------------------------------------------------------------------
function opcoes_Callback(hObject, eventdata, handles)
% hObject    handle to opcoes (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes during object deletion, before destroying properties.
function cxL_DeleteFcn(hObject, eventdata, handles)
% hObject    handle to cxL (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)



function edit7_Callback(hObject, eventdata, handles)
% hObject    handle to tempo (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of tempo as text
%        str2double(get(hObject,'String')) returns contents of tempo as a double


% --- Executes during object creation, after setting all properties.
function edit7_CreateFcn(hObject, eventdata, handles)
% hObject    handle to tempo (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit8_Callback(hObject, eventdata, handles)
% hObject    handle to H (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of H as text
%        str2double(get(hObject,'String')) returns contents of H as a double


% --- Executes during object creation, after setting all properties.
function edit8_CreateFcn(hObject, eventdata, handles)
% hObject    handle to H (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit9_Callback(hObject, eventdata, handles)
% hObject    handle to d (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of d as text
%        str2double(get(hObject,'String')) returns contents of d as a double


% --- Executes during object creation, after setting all properties.
function edit9_CreateFcn(hObject, eventdata, handles)
% hObject    handle to d (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit10_Callback(hObject, eventdata, handles)
% hObject    handle to T (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of T as text
%        str2double(get(hObject,'String')) returns contents of T as a double


% --- Executes during object creation, after setting all properties.
function edit10_CreateFcn(hObject, eventdata, handles)
% hObject    handle to T (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit11_Callback(hObject, eventdata, handles)
% hObject    handle to edit11 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit11 as text
%        str2double(get(hObject,'String')) returns contents of edit11 as a double


% --- Executes during object creation, after setting all properties.
function edit11_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit11 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --------------------------------------------------------------------
function Untitled_2_Callback(hObject, eventdata, handles)
% hObject    handle to Untitled_2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
open('wavekinematics.pdf');



% --------------------------------------------------------------------
function Untitled_3_Callback(hObject, eventdata, handles)
% hObject    handle to Untitled_3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --------------------------------------------------------------------
function saibamais_Callback(hObject, eventdata, handles)
% hObject    handle to saibamais (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
%visible


% --------------------------------------------------------------------
function importardados_Callback(hObject, eventdata, handles)
% hObject    handle to importardados (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --------------------------------------------------------------------
function Untitled_1_Callback(hObject, eventdata, handles)
% hObject    handle to Untitled_1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% --- Executes on button press in pushbutton9.
function pushbutton9_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton9 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
%Recebendo dados do usuário
H = str2double(get(handles.H,'String'));
T = str2double(get(handles.T,'String'));
d = str2double(get(handles.d,'String'));
x = str2double(get(handles.x,'String'));
t = str2double(get(handles.tempo,'String'));

%H=1; T=10; d=50; x=1; t=0;

%Cálculo de comprimento de onda
g =9.81;
W = (4*pi^2*d)/(g*(T^2));
f =1 + (0.666*W + 0.445*W -0.105*W + 0.272*W);
L = (T*sqrt(g*d)*sqrt(f/(1+W*f)));
k = (2*pi/L);
w = (2*pi/T);
c = w/k;
zd = d;

z=0;
for i= 1:zd
    Z(i,1) = z;
    %Calcula a velocidade horizontal 
    uh(i)=(((9.81*k*H)/(2*w))*(cosh(k*(z+zd))/cosh(k*zd))*cos(k*(x-c*t)));
    z = z - 1; 
    
end


UH = uh';
ZUH=[Z,UH];

save('dados_velocidadehorizontal.txt','ZUH','-ascii')

% --- Executes on button press in pushbutton13.
function pushbutton13_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton13 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
H = str2double(get(handles.H,'String'));
T = str2double(get(handles.T,'String'));
d = str2double(get(handles.d,'String'));
x = str2double(get(handles.x,'String'));
t = str2double(get(handles.tempo,'String'));

%H=1; T=10; d=50; x=1; t=0;

%Cálculo de comprimento de onda
g =9.81;
W = (4*pi^2*d)/(g*(T^2));
f =1 + (0.666*W + 0.445*W -0.105*W + 0.272*W);
L = (T*sqrt(g*d)*sqrt(f/(1+W*f)));
k = (2*pi/L);
w = (2*pi/T);
c = w/k;
zd = d;

z=0;
for i= 1:zd
    Z(i,1) = z;
    %Calcula a aceleração vertical 
    Av(i)=(((9.81*k*H)/(2))*(sinh(k*(z+zd))/cosh(k*zd))*cos(k*(x-c*t)));
    z = z - 1; 
    
end
AV = Av';
ZAV=[Z,AV];

save('dados_aceleracaovertical.txt','ZAV','-ascii')



% --- Executes on button press in pushbutton14.
function pushbutton14_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton14 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
H = str2double(get(handles.H,'String'));
T = str2double(get(handles.T,'String'));
d = str2double(get(handles.d,'String'));
x = str2double(get(handles.x,'String'));
t = str2double(get(handles.tempo,'String'));

%H=1; T=10; d=50; x=1; t=0;

%Cálculo de comprimento de onda
g =9.81;
W = (4*pi^2*d)/(g*(T^2));
f =1 + (0.666*W + 0.445*W -0.105*W + 0.272*W);
L = (T*sqrt(g*d)*sqrt(f/(1+W*f)));
k = (2*pi/L);
w = (2*pi/T);
c = w/k;
zd = d;

z=0;
for i= 1:zd
    Z(i,1) = z;
    %Calcula a aceleração horizontal
    Ah(i)=(((9.81*k*H)/(2))*(cosh(k*(z+zd))/cosh(k*zd))*sin(k*(x-c*t)));
    z = z - 1; 
    
end
AH = Ah';
ZAH=[Z,AH];

save('dados_aceleracaohorizontal.txt','ZAH','-ascii')




% --- Executes on button press in pushbutton15.
function pushbutton15_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton15 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in radiobutton11.
function radiobutton11_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton11 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

graficos(handles);


% --- Executes on button press in radiobutton12.
function radiobutton12_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton12 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
graficos(handles);

% --- Executes on button press in pushbutton16.
function pushbutton16_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton16 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
 %EXPORTANDO OS DADOS
H = str2double(get(handles.H,'String'));
T = str2double(get(handles.T,'String'));
d = str2double(get(handles.d,'String'));
x = str2double(get(handles.x,'String'));
t = str2double(get(handles.tempo,'String'));

%Cálculo de comprimento de onda
g =9.81;
W = (4*pi^2*d)/(g*(T^2));
f =1 + (0.666*W + 0.445*W -0.105*W + 0.272*W);
L = (T*sqrt(g*d)*sqrt(f/(1+W*f)));
k = (2*pi/L);
w = (2*pi/T);
c = w/k;
zd = d;

%CHECK BOX - EXPORTAR DADOS
EXPORT1 = get(handles.VelVertical,'Value');
EXPORT2 = get(handles.VelHorizontal,'Value');
EXPORT3 = get(handles.AcelVertical,'Value');
EXPORT4 = get(handles.AcelHorizontal,'Value');

%Elevação da onda
eta = (H/2)*cos(k*x-w*t);
zs = 0;

if EXPORT1 == 1  
    for i= 1:zd+1
        Z(i,1) = zs;
        %Wheeler Stretching
        z = (zs - eta)/(1+eta/zd);
        %Calcula a velocidade vertical
        uv(i)=(((9.81*k*H)/(2*w))*(sinh(k*(z+zd))/cosh(k*zd))*sin(k*(x-c*t))); 
        
        zs = zs - 1; 

    end
    UV = uv';
    ZUV=[Z,UV];

    save('dados_velocidadevertical.txt','ZUV','-ascii')
end


zs=0;
if EXPORT2 == 1 
    for i= 1:zd+1
        Z(i,1) = zs;
        %Wheeler Stretching
        z = (zs - eta)/(1+eta/zd);
        %Calcula a velocidade horizontal 
        uh(i)=(((9.81*k*H)/(2*w))*(cosh(k*(z+zd))/cosh(k*zd))*cos(k*(x-c*t)));
        %uh(i) = (cosh(k*(z+zd))/sinh(k*zd))*(H/2)*w*cos(w*t - k*x); 
        zs = zs - 1; 
    end

    UH = uh';
    ZUH=[Z,UH];

    save('dados_velocidadehorizontal.txt','ZUH','-ascii')
end

zd = d;
zs=0;
if EXPORT3 == 1
    for i= 1:zd+1
        Z(i,1) = zs;
        %Wheeler Stretching
        z = (zs - eta)/(1+eta/zd);
        %Calcula a aceleração vertical
        Av(i)=(((-9.81*k*H)/(2))*(sinh(k*(z+zd))/cosh(k*zd))*cos(k*(x-c*t)));
        zs = zs - 1;
    end
    AV = Av';
    ZAV=[Z,AV];
    
    save('dados_aceleracaovertical.txt','ZAV','-ascii')
end

zd = d;
zs=0;
if EXPORT4 == 1
    for i= 1:zd+1
        Z(i,1) = zs;
        %Wheeler Stretching
        z = (zs - eta)/(1+eta/zd);        
        %Calcula a aceleração horizontal
        Ah(i)=(((9.81*k*H)/(2))*(cosh(k*(z+zd))/cosh(k*zd))*sin(k*(x-c*t)));
        zs = zs - 1;
        
    end
    AH = Ah';
    ZAH=[Z,AH];
    
    save('dados_aceleracaohorizontal.txt','ZAH','-ascii')
end


% --- Executes during object creation, after setting all properties.
function VelHorizontal_CreateFcn(hObject, eventdata, handles)
% hObject    handle to VelHorizontal (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% --- Executes during object creation, after setting all properties.
function VelVertical_CreateFcn(hObject, eventdata, handles)
% hObject    handle to VelHorizontal (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% --- Executes during object creation, after setting all properties.
function text39_CreateFcn(hObject, eventdata, handles)
% hObject    handle to VelHorizontal (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

function graficos (handles)

H = str2double(get(handles.H,'String'));
T = str2double(get(handles.T,'String'));
d = str2double(get(handles.d,'String'));
x = str2double(get(handles.x,'String'));
t = str2double(get(handles.tempo,'String'));

%H=1; T=10; d=50; x=1; t=0;

%Cálculo de comprimento de onda
g =9.81;
W = (4*pi^2*d)/(g*(T^2));
f =1 + (0.666*W + 0.445*W -0.105*W + 0.272*W);
L = (T*sqrt(g*d)*sqrt(f/(1+W*f)));
k = (2*pi/L);
w = (2*pi/T);
c = w/k;
zd = d;

set(handles.cxL, 'String', sprintf('%.2f',L));
set(handles.text10, 'String', sprintf('%.2f',k));
set(handles.text11, 'String', sprintf('%.2f',c));
set(handles.text12, 'String', sprintf('%.2f',w));

%RADIO BUTTON
z =0;
RB1 = get(handles.radiobutton10,'Value');
RB2 = get(handles.radiobutton11,'Value');
RB3 = get(handles.radiobutton12,'Value');
if RB1 == 1 %até L/2
    if(L/2>d)
        zd = d;
        
    else
        zd = L/2;
    end 
end
if RB2 == 1 %até L
    if(L>d)
        zd = d;
        
    else
        zd = L;
    end 
end
if RB3 == 1 %até d
        zd = d;
end

%Elevação da onda
eta = (H/2)*cos(k*x-w*t);
zs = 0;

%VELOCIDADE E ACELERAÇÃO NA PROFUNDIDADE ZERO
uvL0 =(((9.81*k*H)/(2*w))*(sinh(k*(0+zd))/cosh(k*zd))*sin(k*(x-c*t)));
uhL0 = (((9.81*k*H)/(2*w))*(cosh(k*(0+zd))/cosh(k*zd))*cos(k*(x-c*t)));
AhL0 =(((9.81*k*H)/(2))*(cosh(k*(0+zd))/cosh(k*zd))*sin(k*(x-c*t)));
AvL0 =(((-9.81*k*H)/(2))*(sinh(k*(0+zd))/cosh(k*zd))*cos(k*(x-c*t)));

for i= 1:zd+1
    %Wheeler Stretching
    z = (zs - eta)/(1+eta/zd);        
    %Calcula a velocidade horizontal 
    uh(i)=(((9.81*k*H)/(2*w))*(cosh(k*(z+zd))/cosh(k*zd))*cos(k*(x-c*t)));
    %Calcula a velocidade vertical
    uv(i)=(((9.81*k*H)/(2*w))*(sinh(k*(z+zd))/cosh(k*zd))*sin(k*(x-c*t)));
    %Calcula a aceleração vertical 
    Av(i)=(((-9.81*k*H)/(2))*(sinh(k*(z+zd))/cosh(k*zd))*cos(k*(x-c*t)));
    %Calcula a aceleração horizontal
    Ah(i)=(((9.81*k*H)/(2))*(cosh(k*(z+zd))/cosh(k*zd))*sin(k*(x-c*t)));
    
    if(i==1)
        uvL0 = uv(i);
        uhL0 = uh(i);
        AvL0 = Av(i);
        AhL0 = Ah(i);
    end
    
    PERC1(i) = 100*(uv(i)/uvL0);
    PERC2(i) = 100*(uh(i)/uhL0);  
    PERC3(i) = 100*(Av(i)/AvL0);
    PERC4(i) = 100*(Ah(i)/AhL0);
    
    vetori(i)= zs;
    zs = zs - 1;
    
    
end


%Obtendo dados do usuário - CheckBox e RadioButton
VVertical = get(handles.VelVertical,'Value');
VHorizontal = get(handles.VelHorizontal,'Value');
AVertical = get(handles.AcelVertical,'Value');
AHorizontal = get(handles.AcelHorizontal,'Value');

%GRAFICO PERCENTUAL 
cla(handles.axes1,'reset');
cla(handles.axes5,'reset');
hold(handles.axes1,'on');
hold(handles.axes5,'on');

flag1 = 0;
flag2 = 0;

%axis (inf);
j = 1;
if VVertical == 1 
    plot1(j) = plot(uv,vetori,'Parent',handles.axes1,'Color','blue');
    set(plot1(j),'DisplayName','Velocidade Vertical');
    grid (handles.axes1,'on');
    plot2(j)= plot(PERC1,vetori,'Parent',handles.axes5,'Color','blue');
    set(plot2(j),'DisplayName',' Percentual Vel. Vertical'); 
    grid (handles.axes5,'on');
    j = j+1;
    
    flag1 = 1;
    eixox1 = 'Velocidade (m/s)';    
end

if VHorizontal == 1
    plot1(j)= plot(uh,vetori,'Parent',handles.axes1, 'Color','red');
    set(plot1(j),'DisplayName','Velocidade Horizontal');
    grid (handles.axes1,'on');
    plot2(j)=plot(PERC2,vetori,'Parent',handles.axes5, 'Color','red');
    set(plot2(j),'DisplayName',' Percentual Vel. Horizontal'); 
    grid (handles.axes5,'on');
    j=j+1;
    
    if (flag1 == 0)
        eixox1 = 'Velocidade (m/s)';
        flag1 = 1;
    end
end

if AVertical == 1
    plot1(j)= plot(Av,vetori,'Parent',handles.axes1,'Color','green','LineStyle','--');
    set(plot1(j),'DisplayName','Aceleração Vertical');
    grid (handles.axes1,'on');
    plot2(j)=plot(PERC3,vetori,'Parent',handles.axes5, 'Color','green','LineStyle','--');
    set(plot2(j),'DisplayName',' Percentual Acel. Vertical'); 
    grid (handles.axes5,'on');
    j = j+1;
    
    flag2 = 1;
    if (flag1 == 1)
        eixox1 = cat(2,eixox1,', Aceleração (m/s^2)');
    else
        eixox1 = 'Aceleração (m/s^2)';
    end
end

if AHorizontal == 1
    plot1(j)= plot(Ah,vetori, 'Parent',handles.axes1,'Color','black','LineStyle','--');
    set(plot1(j),'DisplayName','Aceleração Vertical');
    grid (handles.axes1,'on');
    plot2(j)=plot(PERC4,vetori,'Parent',handles.axes5,'Color','black','LineStyle','--');
    set(plot2(j),'DisplayName',' Percentual Acel. Horizontal'); 
    grid (handles.axes5,'on');
    j = j+1;
    
    if (flag2 == 0)
        if (flag1 == 1)
            eixox1 = cat(2,eixox1,', Aceleração (m/s^2)');
        else
            eixox1 = 'Aceleração (m/s^2)';
        end 
    end
end

legend1 = legend(handles.axes1,'show');
legend2 = legend(handles.axes5,'show');

if ((flag1 == 1) || (flag2 == 1))
    xlabel(handles.axes1,eixox1);
    ylabel(handles.axes1,'Profundidade (m)');
    xlabel(handles.axes5,'Percentual relativo (%)');
    ylabel(handles.axes5,'Profundidade (m)');
end
