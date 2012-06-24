Summary:	An X Window System based news reader
Summary(pl):	Czytnik news�w pod X Window System
Name:		xrn
Version:	9.02
Release:	11
License:	distributable
Group:		Applications/News
Source0:	ftp://sipb.mit.edu/pub/%{name}/%{name}-%{version}.tgz
Source1:	%{name}.desktop
Patch0:		%{name}-pld.patch
Patch1:		%{name}-glibc.patch
Patch2:		%{name}-time.patch
URL:		http://www.mit.edu/people/jik/software/xrn.html
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
A simple Usenet News reader for the X Window System. Xrn allows you to
point and click your way through reading, replying and posting news
messages.

%description -l pl
Xrn to prosty czytnik news dla X Window System. Xrn pozwala ci na
czytanie artyku��w, odpowiadanie na nie i wysy�anie nowych przy pomocy
myszki.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
xmkmf -a
%{__make} CXXDEBUGFLAGS="%{rpmcflags}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/News

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/News/xrn.spec

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xrn
%config %{_libdir}/X11/app-defaults/XRn
%config %{_applnkdir}/Network/News/xrn.spec
%doc COPYRIGHT COMMON-PROBLMS README README.Linux TODO ChangeLog
