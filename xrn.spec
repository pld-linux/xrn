Summary:	An X Window System based news reader
Summary(cs):	Jednoduch� Newsov� klient pro X Window System
Summary(da):	En X-vinduessystembaseret nyhedsl�ser
Summary(de):	Ein Newsreader f�r das X Window System
Summary(es):	Lector de noticias para X Window
Summary(fr):	Lecteur de nouvelles Usenet pour le syst�me X Window
Summary(id):	News reader yang berbasiskan X Window System
Summary(is):	Fr�ttalesari fyrir X gluggakerfi�
Summary(it):	Un news reader basato su X Window
Summary(ja):	X Window System �١����Υ˥塼���꡼����
Summary(ko):	X ������ �ý��� ��� ���� �б� ���α׷�
Summary(no):	En nyhetsleser for X
Summary(pl):	Czytnik news�w pod X Window System
Summary(pt):	Um leitor de 'news' baseado no X Window System
Summary(ru):	��������� ��� ������ �������� � X Window System
Summary(sk):	Program na ��tanie diskusn�ch skup�n pre syst�m X Window
Summary(sl):	Bralnik novi za Okna X
Summary(sv):	En nyhetsl�sare f�r X11
Summary(zh_CN):	һ������ X ����ϵͳ�������Ķ�����
Name:		xrn
Version:	9.02
Release:	13
License:	distributable
Group:		Applications/News
Source0:	ftp://sipb.mit.edu/pub/%{name}/%{name}-%{version}.tgz
# Source0-md5:	2920543df71c29fda8bb384a7c4f208b
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-pld.patch
Patch1:		%{name}-glibc.patch
Patch2:		%{name}-time.patch
URL:		http://www.mit.edu/people/jik/software/xrn.html
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
A simple Usenet News reader for the X Window System. xrn allows you to
point and click your way through reading, replying and posting news
messages.

%description -l cs
xrn je jednoduch� klient pro �ten� Usenet News v prost�ed� X Window System.

%description -l da
xrn er et simpelt nyhedsprogram for X.

%description -l de
xrn ist ein einfacher Usenet News reader f�r das X Window System.

%description -l es
xrn es un lector sencillo de noticias USENET para X Window.

%description -l fr
xrn est un lecteur de nouvelles Usenet simple pour le syst�me
X Window.

%description -l it
xrn � un news reader di Usenet per X Window.

%description -l ja
xrn �� X Window System �ѤΥ���ץ�� Usenet �˥塼���꡼���Ǥ���

%description -l no
xrn er et enkelt newsprogram for X.

%description -l pl
xrn to prosty czytnik news dla X Window System. xrn pozwala na
czytanie artyku��w, odpowiadanie na nie i wysy�anie nowych przy pomocy
myszki.

%description -l pt
O xrn � um leitor simples de 'news' da Usenet para o X Window System.

%description -l ru
��������� ��� ������ �������� � X Window System.

%description -l zh_CN
xrn ��һ������ X ����ϵͳ�ļ򵥵� Usenet �����Ķ�����.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
xmkmf -a
%{__make} CXXDEBUGFLAGS="%{rpmcflags}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/News,%{_pixmapsdir}}

%{__make} install install.man DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/News/xrn.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/xrn.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT COMMON-PROBLMS README README.Linux TODO ChangeLog
%attr(755,root,root) %{_bindir}/xrn
%config %{_libdir}/X11/app-defaults/XRn
%{_applnkdir}/Network/News/xrn.desktop
%{_pixmapsdir}/xrn.png
%{_mandir}/man1/*
