Summary:	An X Window System based news reader
Summary(cs):	Jednoduchý Newsový klient pro X Window System
Summary(da):	En X-vinduessystembaseret nyhedslæser
Summary(de):	Ein Newsreader für das X Window System
Summary(es):	Lector de noticias para X Window
Summary(fr):	Lecteur de nouvelles Usenet pour le système X Window
Summary(id):	News reader yang berbasiskan X Window System
Summary(is):	Fréttalesari fyrir X gluggakerfið
Summary(it):	Un news reader basato su X Window
Summary(ja):	X Window System ¥Ù¡¼¥¹¤Î¥Ë¥å¡¼¥¹¥ê¡¼¥À¡¼
Summary(ko):	X À©µµ¿ì ½Ã½ºÅÛ ±â¹Ý ´º½º ÀÐ±â ÇÁ·Î±×·¥
Summary(no):	En nyhetsleser for X
Summary(pl):	Czytnik newsów pod X Window System
Summary(pt):	Um leitor de 'news' baseado no X Window System
Summary(ru):	ðÒÏÇÒÁÍÍÁ ÄÌÑ ÞÔÅÎÉÑ ÎÏ×ÏÓÔÅÊ × X Window System
Summary(sk):	Program na èítanie diskusných skupín pre systém X Window
Summary(sl):	Bralnik novi za Okna X
Summary(sv):	En nyhetsläsare för X11
Summary(zh_CN):	Ò»¸ö»ùÓÚ X ´°¿ÚÏµÍ³µÄÐÂÎÅÔÄ¶ÁÆ÷¡£
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
xrn je jednoduchý klient pro ètení Usenet News v prostøedí X Window System.

%description -l da
xrn er et simpelt nyhedsprogram for X.

%description -l de
xrn ist ein einfacher Usenet News reader für das X Window System.

%description -l es
xrn es un lector sencillo de noticias USENET para X Window.

%description -l fr
xrn est un lecteur de nouvelles Usenet simple pour le système
X Window.

%description -l it
xrn è un news reader di Usenet per X Window.

%description -l ja
xrn ¤Ï X Window System ÍÑ¤Î¥·¥ó¥×¥ë¤Ê Usenet ¥Ë¥å¡¼¥¹¥ê¡¼¥À¤Ç¤¹¡£

%description -l no
xrn er et enkelt newsprogram for X.

%description -l pl
xrn to prosty czytnik news dla X Window System. xrn pozwala na
czytanie artyku³ów, odpowiadanie na nie i wysy³anie nowych przy pomocy
myszki.

%description -l pt
O xrn é um leitor simples de 'news' da Usenet para o X Window System.

%description -l ru
ðÒÏÇÒÁÍÍÁ ÄÌÑ ÞÔÅÎÉÑ ÎÏ×ÏÓÔÅÊ × X Window System.

%description -l zh_CN
xrn ÊÇÒ»¸öÓÃÓÚ X ´°¿ÚÏµÍ³µÄ¼òµ¥µÄ Usenet ÐÂÎÅÔÄ¶ÁÆ÷¡£.

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
