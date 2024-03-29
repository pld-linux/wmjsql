Summary:	MySQL monitor for WindowMaker
Summary(pl.UTF-8):	Program dla WindowMakera monitorujący serwer MySQL
Name:		wmjsql
Version:	0.5
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.munsterman.com/%{name}-%{version}.tar.gz
# Source0-md5:	63b3df4cfb5ce3a68fba89c168980995
URL:		http://www.munsterman.com/
BuildRequires:	XFree86-devel
BuildRequires:	mysql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
WindowMaker dock app that monitors the status of a MySQL server.

%description -l pl.UTF-8
Program monitorujący serwer(y) MySQL.

%prep
%setup -q -n wmjsql

%build
cd src
%{__make} clean
%{__make} \
	CXX="%{__cxx}" \
	LD="%{__cxx}" \
	CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D src/wmjsql $RPM_BUILD_ROOT%{_bindir}/wmjsql

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS README TODO src/conf
%attr(755,root,root) %{_bindir}/wmjsql
