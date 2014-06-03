%define oname otter
Name:		otter-browser
Summary:	Web browser controlled by the user, not vice-versa
License:	GPLv3
Version:	0.9.01
Release:	2
Group:		Networking/WWW 
URL:		http://otter-browser.org/
Source:		https://github.com/Emdek/%{oname}/archive/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5Core) >= 5.2
BuildRequires:  pkgconfig(Qt5Network) >= 5.2
BuildRequires:  pkgconfig(Qt5PrintSupport) >= 5.2
BuildRequires:  pkgconfig(Qt5Sensors) >= 5.2
BuildRequires:  pkgconfig(Qt5Sql) >= 5.2
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2
BuildRequires:  pkgconfig(Qt5WebKit) >= 5.2
BuildRequires:  pkgconfig(Qt5WebKitWidgets) >= 5.2
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:	desktop-file-utils
BuildRequires:	qmake5

%description
Browser aiming to recreate classic Opera (12.x) UI using Qt5.


%prep
%setup -qn %{oname}-%{version}
# icon design is done
install -d -m755 %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
install -m644 resources/icons/%{name}-16.png %{buildroot}%{_miconsdir}/%{name}.png
install -m644 resources/icons/%{name}-32.png %{buildroot}%{_iconsdir}/%{name}.png
install -m644 resources/icons/%{name}-48.png %{buildroot}%{_liconsdir}/%{name}.png

%build
%qmake_qt5 
%make

%install
install -Dm755 otter-browser %{buildroot}%{_bindir}/otter-browser

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
   %{name}.desktop

%files
%doc CHANGELOG README.md COPYING TODO HACKING
%{_bindir}/otter-browser
%{_datadir}/applications/%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
