import React, { useState, useEffect } from 'react';

const AnalogDigitalClock = () => {
  const [time, setTime] = useState(new Date());

  useEffect(() => {
    const timer = setInterval(() => {
      setTime(new Date());
    }, 10); // Update every 10ms for smooth animation

    return () => clearInterval(timer);
  }, []);

  const formatTime = (num) => {
    return num.toString().padStart(2, '0');
  };

  const getClockHandRotation = (value, max) => {
    return (value / max) * 360;
  };

  const hours = time.getHours();
  const minutes = time.getMinutes();
  const seconds = time.getSeconds();
  const milliseconds = time.getMilliseconds();

  // Calculate rotations for clock hands
  const secondRotation = getClockHandRotation(seconds + milliseconds / 1000, 60);
  const minuteRotation = getClockHandRotation(minutes + seconds / 60, 60);
  const hourRotation = getClockHandRotation((hours % 12) + minutes / 60, 12);

  // Digital time display
  const digitalTime = `${formatTime(hours)}:${formatTime(minutes)}:${formatTime(seconds)}:${formatTime(Math.floor(milliseconds / 10))}`;

  const ClockNumbers = () => {
    const numbers = [];
    for (let i = 1; i <= 12; i++) {
      const angle = (i * 30 - 90) * (Math.PI / 180);
      const x = 140 * Math.cos(angle);
      const y = 140 * Math.sin(angle);
      
      numbers.push(
        <text
          key={i}
          x={x}
          y={y + 6}
          textAnchor="middle"
          className="fill-blue-800 text-lg font-bold select-none"
        >
          {i}
        </text>
      );
    }
    return numbers;
  };

  const HourMarks = () => {
    const marks = [];
    for (let i = 0; i < 12; i++) {
      const angle = i * 30;
      marks.push(
        <line
          key={i}
          x1="0"
          y1="-160"
          x2="0"
          y2="-145"
          stroke="#1e40af"
          strokeWidth="3"
          transform={`rotate(${angle})`}
        />
      );
    }
    return marks;
  };

  const MinuteMarks = () => {
    const marks = [];
    for (let i = 0; i < 60; i++) {
      if (i % 5 !== 0) { // Skip hour marks
        const angle = i * 6;
        marks.push(
          <line
            key={i}
            x1="0"
            y1="-160"
            x2="0"
            y2="-155"
            stroke="#64748b"
            strokeWidth="1"
            transform={`rotate(${angle})`}
          />
        );
      }
    }
    return marks;
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-indigo-900 flex items-center justify-center p-4">
      <div className="bg-white/10 backdrop-blur-lg rounded-3xl shadow-2xl p-8 border border-white/20">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-white mb-2">Analog Clock</h1>
          <p className="text-blue-200">Live Animated Timepiece</p>
        </div>

        {/* Digital Clock Display */}
        <div className="mb-8 bg-gray-900/50 rounded-xl p-4 border-2 border-blue-400/50">
          <div className="text-center">
            <div className="text-2xl font-mono text-green-400 tracking-wider">
              {digitalTime}
            </div>
            <div className="text-sm text-gray-400 mt-1">
              HH:MM:SS:MS
            </div>
          </div>
        </div>

        {/* Analog Clock */}
        <div className="flex justify-center">
          <div className="relative">
            <svg
              width="400"
              height="400"
              viewBox="-200 -200 400 400"
              className="drop-shadow-2xl"
            >
              {/* Clock Face Background */}
              <circle
                cx="0"
                cy="0"
                r="180"
                fill="#1e293b"
                stroke="#3b82f6"
                strokeWidth="8"
              />
              <circle
                cx="0"
                cy="0"
                r="165"
                fill="#f8fafc"
                stroke="#cbd5e1"
                strokeWidth="2"
              />

              {/* Hour and Minute Marks */}
              <g>
                <HourMarks />
                <MinuteMarks />
              </g>

              {/* Clock Numbers */}
              <g>
                <ClockNumbers />
              </g>

              {/* Clock Hands */}
              {/* Hour Hand */}
              <line
                x1="0"
                y1="0"
                x2="0"
                y2="-80"
                stroke="#1e40af"
                strokeWidth="8"
                strokeLinecap="round"
                transform={`rotate(${hourRotation})`}
                className="transition-transform duration-1000 ease-in-out"
              />

              {/* Minute Hand */}
              <line
                x1="0"
                y1="0"
                x2="0"
                y2="-120"
                stroke="#1e40af"
                strokeWidth="4"
                strokeLinecap="round"
                transform={`rotate(${minuteRotation})`}
                className="transition-transform duration-1000 ease-in-out"
              />

              {/* Second Hand */}
              <line
                x1="0"
                y1="0"
                x2="0"
                y2="-130"
                stroke="#dc2626"
                strokeWidth="2"
                strokeLinecap="round"
                transform={`rotate(${secondRotation})`}
                className="transition-transform duration-75 ease-linear"
              />

              {/* Center Dot */}
              <circle
                cx="0"
                cy="0"
                r="8"
                fill="#1e40af"
                stroke="#ffffff"
                strokeWidth="2"
              />
            </svg>

            {/* Clock Brand */}
            <div className="absolute top-24 left-1/2 transform -translate-x-1/2">
              <div className="text-blue-800 font-bold text-lg">
                MITESH
              </div>
            </div>
          </div>
        </div>

        {/* Additional Time Info */}
        <div className="mt-8 grid grid-cols-3 gap-4 text-center">
          <div className="bg-white/10 rounded-lg p-3 border border-white/20">
            <div className="text-white/70 text-sm">Hours</div>
            <div className="text-white text-xl font-bold">{formatTime(hours)}</div>
          </div>
          <div className="bg-white/10 rounded-lg p-3 border border-white/20">
            <div className="text-white/70 text-sm">Minutes</div>
            <div className="text-white text-xl font-bold">{formatTime(minutes)}</div>
          </div>
          <div className="bg-white/10 rounded-lg p-3 border border-white/20">
            <div className="text-white/70 text-sm">Seconds</div>
            <div className="text-white text-xl font-bold">{formatTime(seconds)}</div>
          </div>
        </div>

        <div className="text-center mt-6">
          <p className="text-white/60 text-sm">
            Real-time analog and digital clock display
          </p>
        </div>
      </div>
    </div>
  );
};

export default AnalogDigitalClock;
