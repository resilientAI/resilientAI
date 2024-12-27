import Image from 'next/image'

export default function WorkHoursViz() {
  return (
    <div className="mt-8">
      <h2 className="text-2xl font-bold mb-4">My Work Hours</h2>
      <div className="relative w-full h-64">
        <Image
          src="/work_hours_viz.png"
          alt="Work Hours Visualization"
          layout="fill"
          objectFit="contain"
        />
      </div>
      <p className="text-sm text-gray-600 mt-2">
        This visualization shows my commit activity over the last 30 days.
      </p>
    </div>
  )
}

